import subprocess
import random
import os

TECHNICAL_TERMS = [
    "refactor: optimización de punteros de memoria y limpieza de descriptores de archivos huérfanos",
    "perf: reestructuración de índices en tablas relacionales para mejorar latencia de consultas",
    "fix: resolución de condiciones de carrera en hilos de ejecución concurrentes",
    "chore: actualización de dependencias críticas y parches de seguridad en contenedores",
    "feat: implementación de estrategia de reintento exponencial en llamadas de red"
]

def create_fake_commit():
    commit_msg = random.choice(TECHNICAL_TERMS)
    
    # Crea un archivo temporal de log local para asegurar que haya cambios en el repo
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
    create_fake_commit()