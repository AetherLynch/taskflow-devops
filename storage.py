import json
import os

FILE_NAME = "tasks.json"

def load_tasks():
    if not os.path.exists(FILE_NAME):
        return []

    try:
        with open(FILE_NAME, "r", encoding="utf-8") as file:
            data = json.load(file)

            # Validar que el contenido sea una lista
            if isinstance(data, list):
                return data
            else:
                print("Error: El archivo JSON no tiene el formato esperado (lista de tareas).")
                return []

    except json.JSONDecodeError:
        print("Error: El archivo JSON está corrupto o mal formado.")
        return []

    except Exception as e:
        print(f"Error inesperado al cargar tareas: {e}")
        return []


def save_tasks(tasks):
    with open(FILE_NAME, "w", encoding="utf-8") as file:
        json.dump(tasks, file, indent=4)
