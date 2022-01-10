def getdate():
    import datetime
    return datetime.datetime.now()

def fitness_func():
    name = input("Enter Your name : ")
    while True:
        entry = int(input("""Choose any of the following options to enter :
                    1. Log New Entry
                    2. Review Old Entries
                    3. Exit
                    """))
        if entry == 3:
            exit()
        elif entry == 1:
            new_entry = int(input("""What do you wish to enter into log book? :
                1. Exercise
                2. Food
                """))
            if new_entry ==2:
                with open(f"{name}-food-log.txt", "a") as f:
                    entry2 = input("Enter the food you ate today :\n")
                    time2 = getdate()
                    f.write(f"{entry2} @ {[str(time2)]} \n")
                    # f.write(str(time2))
                print("Entry Sucessfully Updated.\n")
            elif new_entry == 1:
                with open(f"{name}-exercise-log.txt", "a") as f:
                    entry1 = input("Enter the food you ate today :\n")
                    time1 = getdate()
                    f.write(f"{entry1} @ {[str(time1)]} \n")
                    # f.write(str(time1))
                print("Entry Sucessfully Updated.\n")
        elif entry == 2:
            read_log = int(input("""which log do you wish to review? :
                1. Exercise
                2. Food
                """))
            if read_log == 1:
                with open(f"{name}-exercise-log.txt") as f:
                    print(f.read())
            elif read_log == 2:
                with open(f"{name}-food-log.txt") as f:
                    print(f.read())
        else:
            print("Invalid input. Please choose again.")

fitness_func()