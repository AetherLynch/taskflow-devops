def add_task(tasks, title):
    # Verificar si ya existe una tarea con el mismo título
    for task in tasks:
        if task["title"].lower() == title.lower():
            print("Error: ya existe una tarea con ese título")
            return

    task = {
        "id": len(tasks) + 1,
        "title": title,
        "completed": False
    }
    tasks.append(task)
    print("Tarea agregada")


def list_tasks(tasks):
    if not tasks:
        print("No hay tareas")
        return

    for task in tasks:
        status = "✔" if task["completed"] else "✘"
        print(f'{task["id"]}. {task["title"]} [{status}]')


def complete_task(tasks, task_id):
    for task in tasks:
        if task["id"] == task_id:
            task["completed"] = True
            print("Tarea completada")
            return

    print("Error: ID no encontrado")


def delete_task(tasks, task_id):
    try:
        task_id = int(task_id)
    except:
        print("Error: ID inválido")
        return

    for task in tasks:
        if task["id"] == task_id:
            tasks.remove(task)

            for i, t in enumerate(tasks):
                t["id"] = i + 1

            print("Tarea eliminada")
            return

    print("Error: ID no encontrado")
