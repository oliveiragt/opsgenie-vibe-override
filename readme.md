# 🧞‍♂️ Opsgenie Vibe-Override (The "Not My Problem Anymore" Script)

Bem-vindo ao pináculo da engenharia de software moderna. Este projeto é o resultado de um **trabalho árduo, exaustivo e implacável de exatos 30 minutos**. 

Ele foi 100% **vibecodado** — uma técnica milenar que consiste em ignorar boas práticas, pular a arquitetura e focar puramente nas *vibes* de querer se livrar de um plantão. Escrito a quatro mãos: eu tomando litros de água (para hidratação e sobrevivência) e o Gemini (gastando poder computacional do Google) gerando o código.

## 🎯 O que essa maravilha faz?

Você já esteve de plantão, precisou dar um override no Opsgenie para "Ninguém" (None) e pensou: *"Nossa, eu odeio abrir o navegador e dar 5 cliques para fazer isso"*? Seus problemas acabaram. 

Este script permite que você remova o seu nome do plantão da sua *Rotation* específica pelo terminal, jogando a responsabilidade para o void por exatamente 1 hora.

### ✨ Features (ou "Por que isso existe?")
* **Terminal First:** Porque abrir o navegador gasta muita RAM (e energia mental).
* **Vibecoded Analytics:** Zero testes unitários, 100% de fé.
* **Smart Time Travel:** Se você digitar uma hora que já passou, ele entende que você já está sofrendo por antecipação e agenda pro dia seguinte.
* **Laser Precision:** Limpa o plantão *apenas* na sua Rotation. O coleguinha da outra camada continua sofrendo.

---

## 🚀 Como rodar essa obra de arte

### 1. Pré-requisitos
Certifique-se de ter o Python instalado e instale as dependências (que são surpreendentemente poucas):

```bash
pip install requests python-dotenv
```

### 2. Configurando as Variáveis Secretas
Crie um arquivo chamado `.env` na raiz do projeto. **NÃO COMITE ESSE ARQUIVO**, a menos que você queira que a internet inteira gerencie seus plantões.

```ini
OPSGENIE_API_KEY=sua_chave_genie_aqui_shhh
OPSGENIE_SCHEDULE_ID=nome-do-seu-schedule-no-opsgenie
OPSGENIE_ROTATION_NAME=nome-da-sua-camada-exata
```

### 3. Execução
Rodar o script é mais fácil que explicar pro seu chefe o motivo do alerta ter sido ignorado:

```bash
python override_opsgenie.py
```
O script vai perguntar a hora inicial (formato `HH:MM`). Digite, aperte Enter, e vá ser feliz.

---

## 📜 Disclaimer e Licença

**Aviso Legal:** Este software foi construído à base de água, IA e vontade de dormir. Não me responsabilizo se o servidor pegar fogo durante a exata 1 hora em que o Opsgenie estiver apontando para o "Ninguém".

**Licença:** Faça o que quiser. Se quebrar, você conserta.