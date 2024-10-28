import random

def get_user_choice():
    user_choice = input("Choose (r, p, or s): ").lower()
    return user_choice

def get_computer_choice():
    return random.choice(["r", "p", "s"])

def determine_winner(user_choice, computer_choice):
    if user_choice == computer_choice:
        return "You tied!"
    elif(user_choice == 'r' and computer_choice == 's') or \
        (user_choice == 's' and computer_choice == 'p') or \
        (user_choice == 'p' and computer_choice == 'r'):
        return "You win!"
    else:
        return "You lose!"

def rps_game():
    print("Let's play r, p, s!")

    while True:
        user_choice = get_user_choice()
        computer_choice = get_computer_choice()

        print(f"You chose {user_choice}.")
        print(f"Computer chose {computer_choice}.")

        result = determine_winner(user_choice, computer_choice)
        print(result)

        play_again = input("Play again? (y/n): ").lower()
        if play_again != 'y':
            print("Thanks! Bye!")
            break

if __name__ == "__main__":
    rps_game()