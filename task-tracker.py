import os
import json
from datetime import datetime


def load_tasks():
    if os.path.exists("tasks.json"):
        with open("tasks.json", "r") as file:
            return json.load(file)
    else:
        return []

def save_tasks(tasks):
    with open("tasks.json", "w") as file:
        json.dump(tasks, file)

time_format = "%d-%m-%Y %H:%M:%S"

def timestamp():
    return datetime.now().strftime(time_format)

def find_task(tasks, task_id):
    for task in tasks:
        if task["Id"] == task_id:
            return task
    return None

def status_task(tasks):
    status1 = "todo"
    status2 = "in-progress"
    status3 = "done"

    print("1 .Check the status of the task\n2. Change the status of the task")
    one_or_two = int(input("Choose what would you like to do (Enter 1 or 2): "))
    print("*************************************************")

    if one_or_two == 1:
        print(f"1. {status1}\n2. {status2}\n3. {status3}")
        check = int(input(f"Choose status of the tasks you want to check (Enter 1, 2 or 3): "))
        print("**********************************************")

        count = 0

        for task in tasks:
            if check == 1:
                if task["status"] == status1:
                    count += 1
                    print(f"ID: {task['Id']}, Task: {task['description']}")
            elif check == 2:
                if task["status"] == status2:
                    count += 1
                    print(f"ID: {task['Id']}, Task: {task['description']}")
            elif check == 3:
                if task["status"] == status3:
                    count += 1
                    print(f"ID: {task['Id']}, Task: {task['description']}")
            else:
                print("Please enter a valid choice")

        print(f"\nThe total amount of the task: {count}")

    elif one_or_two == 2:
        find_id = int(input("Choose the ID of the task to change status: "))
        print("*******************************************")
        task = find_task(tasks, find_id)
        if task is None:
            print("Task Id does not exist")
            return
        print(task)

        print(f"1. {status1}\n2. {status2}\n3. {status3}")
        ask_status = input(f"Choose the new status of the task (Enter 1, 2 or 3): ")

        if ask_status == "1":
            task["status"] = status1
            task["updated_at"] = timestamp()
        elif ask_status == "2":
            task["status"] = status2
            task["updated_at"] = timestamp()
        elif ask_status == "3":
            task["status"] = status3
            task["updated_at"] = timestamp()
        else:
            print("Please enter a valid choice")


    save_tasks(tasks)

def create_tasks(tasks):
    new_task = input("Add a new task: ")

    all_id = []
    for task in tasks:
        all_id.append(task["Id"])

    new_id = max(all_id, default=0) + 1

    now = timestamp()
    tasks.append({"Id": new_id, "description": new_task, "status": "todo", "created_at": now, "updated_at": now})

    save_tasks(tasks)

def update_tasks(tasks):
    find_id = int(input("Enter the ID of the task to update: "))
    task = find_task(tasks, find_id)
    if task is None:
        print("Task Id does not exist")
        return
    print(f"Current task: {task['description']}")
    new_text = input("Update the task: ")
    task["description"] = new_text
    task["updated_at"] = timestamp()

    save_tasks(tasks)

def delete_tasks(tasks):
    find_id = int(input("Enter the ID of the task to delete: "))
    task = find_task(tasks, find_id)
    if task is None:
        print("Task Id does not exist")
        return
    print(f"Task was deleted: {task}")

    tasks.remove(task)

    save_tasks(tasks)

def list_tasks(tasks):
    for task in tasks:
        print(task)

is_running = True

def main():
    while is_running:
        print("************")
        print("TASK TRACKER")
        print("************")

        print("____MENU____")
        print("1. Add new tasks")
        print("2. Update tasks")
        print("3. Delete tasks")
        print("4. Status")
        print("5. Show all tasks")

        choice = int(input("Enter your choice(1, 2, 3, 4 or 5): "))
        print("************************************")

        tasks = load_tasks()

        if choice == 1:
            create_tasks(tasks)
        elif choice == 2:
            update_tasks(tasks)
        elif choice == 3:
            delete_tasks(tasks)
        elif choice == 4:
            status_task(tasks)
        elif choice == 5:
            list_tasks(tasks)

        print("********************************************")
        ask_again = input("Do you want to continue? (y/n): ")
        if ask_again == "y":
            continue
        else:
            break


if __name__ == "__main__":
    main()


