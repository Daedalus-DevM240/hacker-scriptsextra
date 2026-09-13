import os
import subprocess
import random
import urllib.request
import json
from datetime import datetime, timedelta
import time

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
    print("Iniciando monitor de standup automático...")
    # Se ejecutará en bucle revisando la hora (Ejemplo configurado para las 09:00 AM de lunes a viernes)
    TARGET_HOUR = 9
    TARGET_MINUTE = 0

    while True:
        now = datetime.now()
        # Lunes a Viernes (0 a 4) y hora exacta
        if now.weekday() < 5 and now.hour == TARGET_HOUR and now.minute == TARGET_MINUTE:
            generate_fake_standup()
            # Duerme 61 segundos para evitar múltiples envíos en el mismo minuto
            time.sleep(61)
        else:
            # Revisa cada 30 segundos
            time.sleep(30)