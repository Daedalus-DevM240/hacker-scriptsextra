import subprocess
import random
import os
import time

TECHNICAL_TERMS = [
    "refactor: optimización de punteros de memoria y limpieza de descriptores de archivos huérfanos",
    "perf: reestructuración de índices en tablas relacionales para mejorar latencia de consultas",
    "fix: resolución de condiciones de carrera en hilos de ejecución concurrentes",
    "chore: actualización de dependencias críticas y parches de seguridad en contenedores",
    "feat: implementación de estrategia de reintento exponencial en llamadas de red"
]

def create_fake_commit():
    commit_msg = random.choice(TECHNICAL_TERMS)
    log_file = "system_diagnostic.log"
    with open(log_file, "a") as f:
        f.write(f"Diagnostic check executed at internal node.\n")
        
    try:
        subprocess.run(["git", "add", log_file], check=True)
        subprocess.run(["git", "commit", "-m", commit_msg], check=True)
        print(f"Commit falso generado y registrado: '{commit_msg}'")
    except Exception as e:
        print(f"Error al ejecutar git: {e}")

if __name__ == "__main__":
    print("Iniciando servicio de commits automáticos en segundo plano...")
    while True:
        create_fake_commit()
        # Espera 24 horas (86400 segundos) antes del siguiente commit
        # Puedes cambiarlo a otro valor, por ejemplo, 3600 para 1 hora
        time.sleep(86400)