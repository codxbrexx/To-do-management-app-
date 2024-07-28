def tasks():
  tasks = []
  print("------WELCOME TO THE TASK MANAGEMENT APP------")

  total_task = int(input("Enter how many task you want to add :"))
  for i in range(1, total_task+1):
     task_name = input(f"Enter task {i} : ")
     tasks.append(task_name)
  print(f"Today's task are : {tasks}")
 
  while True:
     operation = int(input("your Choice :\n1-Add\n2-Update\n3-Delete\n4-View\n5-Exit/Stop\n Enter : "))
     if  operation == 1:
         add = input("Enter task you want to add : ")
         tasks.append(add)
         print(f"task {add} has been Successfully added...")
         print(f"Today's task are : {tasks}")


     elif operation == 2:
         updated_val = input("Enter the task name you wnat to update : ")
         if updated_val in tasks:
            up = input("Enter new task : ")
            ind = tasks.index(updated_val)
            tasks[ind] = up
            print(f"Updated task {up}")
            print(f"Today's task are : {tasks}")
         else:
            print("Task not found")

     elif operation == 3:
        del_val = input("Which task you want to delete :")
        if del_val in tasks:
          ind = tasks.index(del_val)
          del tasks[ind]
          print(f"Task {del_val} has been deleted...")
          print(f"Today's task are : {tasks}")
      
        else:
          print("Task not found")


     elif operation == 4:
          print(f"Today's task are : {tasks}")

     elif operation == 5:
       print("The programe has been stoped...\n...........Thank you for using the Programe................")
       break

     else: 
       print("Invalid Input")   

tasks()

