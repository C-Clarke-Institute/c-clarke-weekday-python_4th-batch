
#
# 1 add task
# 2. view task
# 3. remove task
# 4. exit

to_do_list = []

while 1 :
    print("\n ===== To Do List =====")

    user_input = int(input("\n1. Add Task "
                           "\n2. View Tasks"
                           "\n3.Remove Task"
                           "\n4.Exit \n"))


    if user_input == 1:
        new_task = input("Enter the New Task : ")
        to_do_list.append(new_task)

    elif user_input == 2:
        for i in range(len(to_do_list)):
            print(f"{i + 1}. {to_do_list[i]}")
    elif user_input == 3:

        for i in range(len(to_do_list)):
            print(f"{i + 1}. {to_do_list[i]}")

        remove_task = int(input("Enter task number to remove : ")) -1
        print(f"{to_do_list[remove_task]} removed from the list ....")
        del to_do_list[remove_task]

    elif user_input == 4:
        exit()

    else:
        print("Invalid Input ")