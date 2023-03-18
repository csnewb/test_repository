import random


def new_number(to_number):
    number = random.randint(0, to_number + 1)
    return number


def new_guess(current_guess, to_number):

    def get_guess():
        valid_answer = False
        while not valid_answer:
            try:
                answer = int(input(f"Current Guess: {current_guess}      Guess a number to continue:  "))
                valid_answer = True
            except ValueError as e:
                if str(e) == "invalid literal for int() with base 10: 'end'" or \
                        str(e) == "invalid literal for int() with base 10: 'End'" or \
                        str(e) == "invalid literal for int() with base 10: 'EXIT'":
                    print("Exiting...")
                    exit()
                elif str(e) == "invalid literal for int() with base 10: 'reset'" or \
                        str(e) == "invalid literal for int() with base 10: 'Reset'" or \
                        str(e) == "invalid literal for int() with base 10: 'RESET'":
                    print("Starting Over with New Game...")
                    new_game()
                else:
                    print("Error: Invalid input. Please enter a number.")
                    valid_answer = False
        return answer

    answer = get_guess()
    if answer < 1 or answer > to_number:
        print(f"Error: Invalid input. Please enter a number between 1 and {to_number}")
        get_guess()
    return answer


def check_menu(menu_count):
    if menu_count > 9:
        print("\nMENU --- | END : to exit  | RESET : to start over  | --- \n")
        menu_count = 0
    return menu_count


def get_to_number():
    try:
        to_number = int(input(f"Please select the max number for the guessing range (between 1 and __):  "))
    except ValueError:
        print("Error: Invalid input. Please enter a number.")
    return to_number


def check_if_keep_playing(number, answer):
    if number == answer:
        return False
    else:
        return True


def player_feedback(number, answer):
    if answer < number:
        print(f"The answer is HIGHER than your guess of {answer}")
    if answer > number:
        print(f"The answer is LOWER than your guess of {answer}")


def new_game():
    print("\n", f"     ---- Welcome to Guessing Game ----", "\n")
    keep_playing = True
    menu_count = 10
    guesses = 0
    to_number = get_to_number()
    number = new_number(to_number)

    while keep_playing:
        menu_count = check_menu(menu_count)
        current_guess = guesses + 1
        answer = new_guess(current_guess, to_number)
        keep_playing = check_if_keep_playing(number, answer)
        if not keep_playing:
            print("\n",  f"Congratulations, you've won! Number was: {number} and you took {current_guess} guesses")
            play_again = input(f"\nWould you like to play again? Yes to continue anything else to exit: ")
            if play_again.lower() == "yes" or "y":
                print("\n"*3)
                new_game()
            else:
                exit()
        else:
            player_feedback(number, answer)
            guesses += 1
            menu_count += 1
# Another way to approach this would be to accept answer as a raw input, then use a comparitive function
# to see if it is a string or int, then if string check if its a menu word, and if int then pass it to the
# check answer function... probably a better way to go to avoid highjacking the ValueError as an evaluator



#################### Run ######################

if __name__ == "__main__":
    new_game()

