import os
import subprocess
import random
from datetime import datetime, timedelta
import time

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

def generate_local_standup():
    commits = get_yesterday_commits()
    if not commits:
        excuse = random.choice(CORPORATE_WORDS)
        commits = f"- Analizando arquitectura de sistemas y {excuse}."
    
    # Estructura del reporte
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    report = f"""==================================================
🤖 Standup Automático de Daedalus [{timestamp}]
--------------------------------------------------
*Ayer hice:* 
{commits}

*Hoy haré:* 
Continuar con el despliegue de infraestructura y revisión de dependencias.
==================================================\n\n"""

    # Muestra el reporte en consola
    print(report)

    # Guarda el reporte en un archivo de texto local llamado 'standup_log.txt'
    log_filename = "standup_log.txt"
    with open(log_filename, "a", encoding="utf-8") as f:
        f.write(report)
    
    print(f"Reporte guardado exitosamente en '{log_filename}'")

if __name__ == "__main__":
    print("Iniciando monitor de standup local...")
    
    # Configurado para ejecutarse a una hora específica (Ejemplo: 09:00 AM)
    TARGET_HOUR = 9
    TARGET_MINUTE = 0

    while True:
        now = datetime.now()
        # Lunes a Viernes (0 a 4) y hora exacta
        if now.weekday() < 5 and now.hour == TARGET_HOUR and now.minute == TARGET_MINUTE:
            generate_local_standup()
            time.sleep(61)  # Duerme un minuto para evitar duplicados
        else:
            time.sleep(30)  # Revisa el reloj cada 30 segundos