from tasks import (
    add_task,
    list_tasks,
    complete_task,
    delete_task
)
from storage import load_tasks, save_tasks
from utils import show_menu

tasks = []

def main():
    global tasks
    tasks = load_tasks()

    while True:
        show_menu()
        option = input("Selecciona una opción: ")

        #  Validar que sea un número
        if not option.isdigit():
            print("Error: Debes ingresar un número.")
            continue

        #  Validar rango de opciones
        if option not in ["1", "2", "3", "4", "5"]:
            print("Error: Opción fuera de rango.")
            continue

        if option == "1":
            title = input("Título de la tarea: ")
            add_task(tasks, title)

        elif option == "2":
            list_tasks(tasks)

        elif option == "3":
            task_id = input("ID de la tarea a completar: ")
            complete_task(tasks, task_id)

        elif option == "4":
            task_id = input("ID de la tarea a eliminar: ")
            delete_task(tasks, task_id)

        elif option == "5":
            save_tasks(tasks)
            print("¡Hasta luego!")
            break

        else:
            print("Opción inválida")

        save_tasks(tasks)

if __name__ == "__main__":
    main()
