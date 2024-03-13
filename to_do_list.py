def to_do_list():
    data = []
    print('''Menu:
1.Add Task
2.Mark Task as Done
3.View your Pending Tasks
4.Exit''')
    user_input = input("Enter Your Choice : ")
    while(user_input != 4)
        if(user_input == 1):
            task = input("What task you have to complete?")
            data.append(task)
            print("Your Task Added Successfully into ToDo List")
        elif(user_input == 2):
            completed = input("What task you are Completed?")
            if completed in data:
                data.remove(completed)
                print("Your completed task is marked as done")
                print("Your Remaining Tasks are ",data)
            else:
                print("Provided Task is not in Your To-Do List")
        elif(user_input == 3):
            print("Your Remaining Tasks are ",data)
    print("GoodBye! Have a Nice Day!")

to_do_list()
