tasks = {
    "прибрати кімнату": "виконано",
    "написати звіт": "в процесі",
    "відвідати лікаря": "очікує"
}

def add_task(name, status="очікує"):
    if name not in tasks:
        tasks[name] = status
    else:
        print(f"Задача '{name}' вже існує.")

def remove_task(name):
    if name in tasks:
        del tasks[name]
    else:
        print(f"Задача '{name}' не знайдена.")

def update_status(name, new_status):
    if name in tasks:
        tasks[name] = new_status
    else:
        print(f"Задача '{name}' не знайдена.")

add_task("купити продукти")
update_status("написати звіт", "виконано")
remove_task("прибрати кімнату")

waiting_tasks = [task for task, status in tasks.items() if status == "очікує"]

print("Список задач:")
print(tasks)

print("\nЗадачі зі статусом 'очікує':")
print(waiting_tasks)
