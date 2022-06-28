import random

def header():
    print("-------------------------------")
    print("Welcome to the FizzBuzz Program")
    print("-------------------------------")
    print("Choose a way to get a number: \n")

def choice_menu():
    print("\n1. Let the computer pick")
    print("2. Manually enter a number")
    print("3. Exit\n")

    your_choice = int(input("Enter your choice: "))
    return your_choice

# Computer that prints the numbers from 1 to 100.
def computer_choice():
    num = random.randint(1, 100)
    return num

# Manually enters a number from 1-100.
def manual_choice():
    num = int(input("Enter a number from 1-100: "))
    if num < 1 or num > 100:
        print ("Please enter number only from 1-100")
        return manual_choice()
    else:
        return num

# Get the number from computer or manual input
def get_number():
    choice = choice_menu()
    if choice == 1:
        return computer_choice()
    elif choice == 2:
        return manual_choice()
    elif choice == 3:
        exit()
    else:
        print("Please enter a valid choice")
        return get_number()

# define if the number is fizz, buzz or fizzbuzz
def fizz_buzz(num):
    if num % 15 == 0:
        return ("FizzBuzz")
    elif num % 3 == 0:
        return ("Fizz")
    elif num % 5 == 0:
        return ("Buzz")
    else:
        return("neither multiples of three or five")

def main():
    header()
    num = get_number()
    fizz_or_buzz = fizz_buzz(num)
    print(f"\nThe number chosen was {num}, it is {fizz_or_buzz}")

main()