import os

FILE_NAME = "TaskList.txt"

# save task to file
def load_task():
    task ={}
    if os.path.exists(FILE_NAME):
        with open(FILE_NAME,"r") as file :
            for line in file :
                task_id , title , string = line.strip().split("/")
                task[ int (task_id)]= {"title":title,"string":string}
    return task


def save_file (task):
    with open(FILE_NAME,"w") as file :
        for task_id in task:
            file.write(f"{task_id}/{task[task_id]['title']}/{task[task_id]['string']}\n")


def add_task(task):
    titel = input("Enter task title : ")
    string = input("Enter task string : ")
    task_id = max(task.keys(),default=0)+1
    task[task_id] = {"title":titel,"string":string}
    print(f"Task{titel},added successfully")
    return task


def view_task(task):
    if not task:
        print("No task found")
    else:
        for task_id in task:
            print(f"[{task_id}]/{task[task_id]['title']}/{task[task_id]['string']}")

    return task

def mark_task_complet(task):
    task_id = int(input("Enter task id : "))
    if task_id in task:
        task[task_id]["string"] = "complete"
        print(f"Task '{task[task_id]["status"]}'matked as complete")
    else:
        print("Task not found")
    return task



def delete_task(task):
    task_id = int(input("Enter task id : "))
    if task_id in task:
        delete_task= task.pop(task_id)
        print(f"Task '{task[task_id]['title']}' deleted successfully")
    else :
        print("Task not found")
    return task



def main():
    task = load_task()
    while True:
        print("1.Add Task")
        print("2.View Task")
        print("3.Mark Task Complete")
        print("4.Delete Task")
        print("5.Save and Exit")
        choice = input("Enter your choice : ")
        if choice == "1":
            task = add_task(task)
        elif choice == "2":
            task = view_task(task)
        elif choice == "3":
            task = mark_task_complet(task)
        elif choice == "4":
            task = delete_task(task)
        elif choice == "5":
            save_file(task)
            print("Task saved successfully and exited")
            break 
        else:
            print("Invalid choice")


if __name__ == "__main__":
    main()
