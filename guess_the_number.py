import random
import time

# ANSI escape codes for text colors
RED = "\033[91m"  # For "TOO HIGH"
BLUE = "\033[94m"  # For "TOO LOW"
RESET = "\033[0m"  # Reset color to default


def get_difficulty():
    while True:
        print("Choose a difficulty level:")
        print("1. Easy (Time limit: 30 seconds, Number range: 0-50)")
        print("2. Medium (Time limit: 20 seconds, Number range: 0-100)")
        print("3. Hard (Time limit: 10 seconds, Number range: 0-200)")

        choice = input("Enter the number corresponding to your chosen difficulty: ")
        if choice in ["1", "2", "3"]:
            return int(choice)
        else:
            print("Invalid choice. Please try again.")

def calculate_score(attempts, time_elapsed, difficulty):
    # Calculate score based on attempts, time, and difficulty level
    base_score = 1000
    attempts_score = max(0, (10 - attempts) * 100)  # Bonus for fewer attempts
    time_score = max(0, (20 - time_elapsed) * 50)   # Bonus for faster time

    # Adjust score based on difficulty level
    if difficulty == 1:
        difficulty_multiplier = 1
    elif difficulty == 2:
        difficulty_multiplier = 1.5
    else:
        difficulty_multiplier = 2

    final_score = int(base_score + attempts_score + time_score) * difficulty_multiplier
    return final_score

def game():
    difficulty = get_difficulty()

    if difficulty == 1:
        time_limit = 30
        number_range = 50
    elif difficulty == 2:
        time_limit = 20
        number_range = 100
    else:           # difficulty == 3
        time_limit = 10
        number_range = 200

    secret_number = random.randint(0, number_range)
    attempts = 0

    print('Welcome to "guess the number" game!')
    print("You have to guess the number chosen by the computer.")
    print(f"You have {time_limit} seconds to guess the number.")
    print(f"The number is between 0 and {number_range}. \n")

    start_time = time.time()
    print("This is your start time:", time.strftime("%Y-%m-%d %H:%M:%S")) #represent the time as a string

    while True:
        try:
            time_elapsed = time.time() - start_time
            time_left = time_limit - time_elapsed # to show the time left 

            print("This is your time left:", "{:.2f}".format(time_left), "seconds") #time left shown in decimal 

            if time_left <= 0:
                print("Time limit exceeded! The secret number was:", secret_number, "\n")
                break

            guess = int(input(f"Enter a number between 0 and {number_range}: \n"))
            attempts += 1

            if guess > number_range or guess < 0:
                print(f"Please enter a number BETWEEN 0 AND {number_range}! \n")
                continue

            if guess == secret_number:
                print("You won!")
                print("The secret number is", secret_number, "\n")
                print("Number of attempts:", attempts)
                print("Time taken:", int(time_elapsed), "seconds")

                score = calculate_score(attempts, time_elapsed, difficulty)
                print("Your score:", score)
                break

            elif guess > secret_number:
                print( RED + "Your number is TOO HIGH, try again! \n" + RESET )

            else:
                print( BLUE + "Your number is TOO LOW, try again! \n" + RESET )

        except ValueError:
            print("Please enter a valid number! \n")

    play_again = input("Do you want to play again? (yes/no): \n ")
    if play_again.lower() == "yes":
        game()
    else:
        print("Thank you for playing! \n")

if __name__ == "__main__":
    game()
