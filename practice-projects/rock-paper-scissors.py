def game():
    def exit_game():
        print("\nThank you for playing the game.")
        print(f"Computer won {comp_win} times.")
        print(f"You won {user_win} times.")
        if comp_win == user_win:
            print("The final resuls is : Its a Tie!")        
        elif comp_win < user_win:
            print("The final resuls is : YOU WIN!")
        else:
            print("The final resuls is : COMPUTER WINS!")
        return exit()
    
    import random
    print("***** Welcome to the game called [Rock/Paper/Scissors] *****")
    comp_win = 0
    user_win = 0
    
    while True:
        # a = random.randint(1,3)
        # if a == 1:
        #     comp_guess = "r"
        # elif a == 2:
        #     comp_guess = "p"
        # elif a == 3:
        #     comp_guess = "s"
        a = random.choice(["r", "p", "s"])          # choose either of the 2 methods
        comp_guess = a
        print("Computer has made his move, Its your turn now.\n")

        user_input= input("""Enter your value:
            'r' for rock
            'p' for paper
            's' for scissors
            'e' for exiting the game.
            """)

        if user_input == "e":
            exit_game()
        elif user_input == comp_guess:
            print(f"You choose {user_input}")
            print(f"computer chose {comp_guess}")
            print("It's a TIE!")
        elif user_input == "r" and comp_guess == "p":
            print(f"You choose {user_input}")
            print(f"computer chose {comp_guess}")
            print("Computer wins!")
            comp_win += 1
        elif user_input == "s" and comp_guess == "r":
            print(f"You choose {user_input}")
            print(f"computer chose {comp_guess}")
            print("Computer wins!")
            comp_win += 1
        elif user_input == "p" and comp_guess == "s":
            print(f"You choose {user_input}")
            print(f"computer chose {comp_guess}")
            print("Computer wins!")
            comp_win += 1
        else:
            print(f"You choose {user_input}")
            print(f"computer chose {comp_guess}")
            print('You Win!')
            user_win +=1

        print("\nDo you wish to play again?") 
        b = input("'Y' for YES or 'N' for NO) : ").lower()
        if b == "y":
            continue
        else:
            exit_game()

game()