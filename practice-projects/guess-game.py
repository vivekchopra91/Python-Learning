import random

computer_guess = random.randint(1,100)
# print(a)
print("Welcome to the number guessing game.")
print("you get total of 9 guesses.")
guesses = 9
i = 0
while True:
    user_guess = int(input("Enter any number b/w [1 - 100] : "))
    i+=1
    if guesses == 0:
        print("You used up all your guesses.")
        print("Game Over!")
        break
    elif user_guess == computer_guess:
        print("Congratulations! You Won.")
        print(f"You guessed the number in {i} guesses.")
        break
    elif user_guess < computer_guess :
        print("Your guess was wrong. ")
        print(f"You have {9-i} guesses left")
        print("Please enter a higher number.\n")
    elif user_guess > computer_guess : 
        print("Your guess was wrong. ")
        print(f"You have {9-i} guesses left")
        print("Please enter a lower number.\n")
    else:
        print("Please enter a valid input.\n")
        print(f"You have {9-i} guesses left")
    guesses -= 1