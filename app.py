def task():
    tasks =[]  #empty list
    print("--Welcome To The Task Management App--")


    total_task= int(input("Enter how many task you want to add = "))
    for i in range (1, total_task+1):
        task_name = input(f"Enter task {i} = ")
        task.append(task_name)

    print(f"Todays tasks are\n {tasks}")

    while True:
        operation= int(input("Enter\n1-Add\n2-Update\n3-Delete\n4-View\n5-Exit/Stop"))
       
        if operation ==1:
            add =input("Enter the task you want to add =")
            tasks.append(add)
            print(f"task {add} has been sucessfully added...!")

        elif operation ==2:
            updated_val =input("Enter the task name you want to update = ")
            if updated_val in tasks:
                up =input("Enter th new task = ")
                ind = tasks.index(updated_val)
                tasks[ind]= up
                print(f"Updated Task {up}")





