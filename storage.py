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
        if not isinstance(data, list):
            print("Error: El archivo JSON no contiene una lista de tareas.")
            return []

        # Validar estructura básica de cada tarea
        for task in data:
            if not isinstance(task, dict):
                print("Error: Formato de tarea inválido.")
                return []

            if not all(key in task for key in ("id", "title", "completed")):
                print("Error: Una o más tareas tienen campos faltantes.")
                return []

        return data

    except json.JSONDecodeError:
        print("Error: El archivo JSON está corrupto o mal formado.")
        return []

    except Exception as e:
        print(f"Error inesperado al cargar tareas: {e}")
        return []


def save_tasks(tasks):
    with open(FILE_NAME, "w", encoding="utf-8") as file:
        json.dump(tasks, file, indent=4)
