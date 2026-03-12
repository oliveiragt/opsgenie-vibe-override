import os
import sys
from datetime import datetime, timedelta
import requests
from dotenv import load_dotenv

# Carrega as variáveis de ambiente
load_dotenv()

API_KEY = os.getenv("OPSGENIE_API_KEY")
SCHEDULE_NAME = os.getenv("OPSGENIE_SCHEDULE_ID")
ROTATION_NAME = os.getenv("OPSGENIE_ROTATION_NAME")

BASE_URL = "https://api.opsgenie.com" 

def check_env_vars():
    if not all([API_KEY, SCHEDULE_NAME, ROTATION_NAME]):
        print("Erro: Variáveis de ambiente ausentes.")
        print("Certifique-se de definir OPSGENIE_API_KEY, OPSGENIE_SCHEDULE_ID e OPSGENIE_ROTATION_NAME.")
        sys.exit(1)

def get_uuids():
    """Busca os UUIDs oficiais do Schedule e da Rotation."""
    print(f"Buscando dados do schedule '{SCHEDULE_NAME}'...")
    endpoint = f"{BASE_URL}/v2/schedules/{SCHEDULE_NAME}"
    headers = {"Authorization": f"GenieKey {API_KEY}"}
    params = {"identifierType": "name"}
    
    try:
        response = requests.get(endpoint, headers=headers, params=params)
        response.raise_for_status()
        data = response.json()["data"]
        
        schedule_uuid = data["id"]
        rotation_uuid = None
        
        # Procura a rotation específica dentro do schedule
        for rot in data.get("rotations", []):
            if rot["name"] == ROTATION_NAME:
                rotation_uuid = rot["id"]
                break
                
        if not rotation_uuid:
            print(f"\n❌ Erro: Rotation '{ROTATION_NAME}' não encontrada.")
            print("Verifique se o nome digitado no .env é exatamente igual ao do Opsgenie.")
            sys.exit(1)
            
        return schedule_uuid, rotation_uuid
        
    except requests.exceptions.HTTPError as err:
        print(f"\n❌ Erro ao buscar o Schedule.")
        print(f"Detalhes: {response.text}")
        sys.exit(1)

def get_time_input():
    print("\nDefina o horário de início para remover o plantão (Duração: 1 hora).")
    user_input = input("Digite a hora no formato HH:MM (ex: 14:30): ")
    
    try:
        now = datetime.now().astimezone()
        parsed_time = datetime.strptime(user_input, "%H:%M")
        
        start_time = now.replace(
            hour=parsed_time.hour, 
            minute=parsed_time.minute, 
            second=0, 
            microsecond=0
        )
        
        if start_time < now:
            print("⚠️ O horário já passou hoje. Agendando para amanhã...")
            start_time += timedelta(days=1)
            
        return start_time
    except ValueError:
        print("Erro: Formato de hora inválido. Siga o padrão HH:MM.")
        sys.exit(1)

def create_override(start_time, schedule_uuid, rotation_uuid):
    end_time = start_time + timedelta(hours=1)
    
    start_iso = start_time.isoformat()
    end_iso = end_time.isoformat()
    
    endpoint = f"{BASE_URL}/v2/schedules/{schedule_uuid}/overrides"
    headers = {
        "Authorization": f"GenieKey {API_KEY}",
        "Content-Type": "application/json"
    }
    
    # Payload com a Rotation Especificada
    payload = {
        "user": {
            "type": "none"
        },
        "startDate": start_iso,
        "endDate": end_iso,
        "rotations": [
            {
                "id": rotation_uuid
            }
        ]
    }

    print(f"\nLimpando apenas a rotation '{ROTATION_NAME}'...")
    print(f"Início: {start_iso}")
    print(f"Fim:    {end_iso}")
    
    try:
        response = requests.post(endpoint, headers=headers, json=payload)
        response.raise_for_status() 
        
        data = response.json()
        print("\n✅ Sucesso! O override foi aplicado APENAS na sua rotation.")
        print(f"ID do Override: {data.get('data', {}).get('alias') or 'Desconhecido'}")
        
    except requests.exceptions.HTTPError as err:
        print(f"\n❌ Erro na API do Opsgenie: {err}")
        print(f"Detalhes: {response.text}")

if __name__ == "__main__":
    check_env_vars()
    
    # Busca ambos os UUIDs necessários
    sched_uuid, rot_uuid = get_uuids()
    
    override_start = get_time_input()
    create_override(override_start, sched_uuid, rot_uuid)