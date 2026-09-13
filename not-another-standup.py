import os
import subprocess
import random
import urllib.request
import json
from datetime import datetime, timedelta

# Configura tu Webhook de Slack o Teams aquí o mediante variables de entorno
WEBHOOK_URL = os.environ.get("STANDUP_WEBHOOK_URL", "https://hooks.slack.com/services/TU/WEBHOOK/REAL")

CORPORATE_WORDS = [
    "optimizando la sinergia de microservicios",
    "refactorizando pipelines de integración continua",
    "mitigando deuda técnica heredada",
    "escalando la resiliencia del clúster",
    "asegurando la cobertura de integración asíncrona"
]

def get_yesterday_commits():
    yesterday = (datetime.now() - timedelta(days=1)).strftime("%Y-%m-%d")
    try:
        cmd = f'git log --since="{yesterday} 00:00:00" --until="{yesterday} 23:59:59" --author="$(git config user.name)" --pretty=format:"- %s"'
        result = subprocess.check_output(cmd, shell=True, text=True)
        return result.strip()
    except Exception:
        return ""

def generate_fake_standup():
    commits = get_yesterday_commits()
    if not commits:
        excuse = random.choice(CORPORATE_WORDS)
        commits = f"- Analizando arquitectura de sistemas y {excuse}."
    
    message = {
        "text": f"🤖 *Standup Automático de Daedalus*:\n*Ayer hice:* \n{commits}\n*Hoy haré:* Continuar con el despliegue de infraestructura y revisión de dependencias."
    }
    
    req = urllib.request.Request(
        WEBHOOK_URL,
        data=json.dumps(message).encode('utf-8'),
        headers={'Content-Type': 'application/json'}
    )
    try:
        urllib.request.urlopen(req)
        print("Standup enviado con éxito.")
    except Exception as e:
        print(f"Error al enviar el standup: {e}")

if __name__ == "__main__":
    generate_fake_standup()