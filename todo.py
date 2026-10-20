tasks=[]
next_id=1

def addtask():
    global next_id

    task_name=input("Enter your Task:")
    if task_name.strip()=="":
        print("Task name cannot be empty")
        return

    task={
        "id":next_id,
        "Task":task_name,
        "Status":"Pending"
    }
    tasks.append(task)
    next_id +=1
    print("Task Added successfully:")
    print("Task:", task)

def viewtask():
     print("\nAll Tasks")
     if len(tasks)==0:
        print("No task Available.")
     else:
         for task in tasks:
            print("Task:", task["id"])
            print("Task Name:", task["Task"])
            print("Status:", task["Status"])
            print("-"*10)

def update_task():
    try:
        task_id=int(input("Enter your task id:"))
    except ValueError:
        print("Please enter number only.")
        return
    found=False
    for task in tasks:
        if task["id"]==task_id:
            found=True
            new_task=input("Enter a new task:")
            task["Task"]=new_task
            print("Task updated succesfully.")
            print("Task", task)
            break
    if found==False:
            print("Id not found..")

def delete_task():
    try:
        task_id=int(input(" Enter your id:"))
    except ValueError:
         print("Please enter numbers only!")
         return
    found=False
    for task in tasks:
        if task["id"]==task_id:
            tasks.remove(task)
            found=True
            print("Task deleted successfully.")
            break
    if found==False:
        print("Id not found.")

def complete_task():
    try:
         task_id=int(input("Enter your id:"))
    except ValueError:
        print("Please enter numbers only!")
        return
    found=False
    for task in tasks:
        if task["id"]==task_id:
            task["Status"]="Completed"
            found=True
            print("Your completed task")
            print("Task:",task)
            break
    if found== False:
        print("id not found.")


while True:
    print("1.Add Tasks")
    print("2.View Tasks")
    print("3.Update Tasks")
    print("4.Delete Tasks")
    print("5.Complete Tasks")
    print("6.exit")
    try:
        choice=int(input("Enter your choice:"))
    except ValueError:
        print("Please enter numbers only!")
    if choice==1:
        addtask()
    elif choice==2:
        viewtask()
    elif choice==3:
        update_task()
    elif choice==4:
      delete_task()
    elif choice==5:
       complete_task()
    elif choice==6:
            print("Thank you for using Todo app!")
            break
    else:
        print("Invaild choice! Please try again.")
 
        
        

