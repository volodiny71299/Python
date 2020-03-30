# Higher or lower game
# Format for guess info


def h1_statement(statement, char):
    # print()
    print(char * len(statement))
    print(statement)
    print(char * len(statement))
    print()


# Makes sure guess is in range of min and max (1 and 10)


def int_check(question, low, high):
    valid = False
    while not valid:

        try:
            response = int(input(question))
            if low <= response <= high:
                print()
                return response
            else:
                print("Enter a number between {} and {}\n".format(low, high))

        except ValueError:
            print("Please Enter An Integer.\n")

# Start of keep going loop


keep_going = ""
while keep_going == "":

    import random

    # Defines low and high values
    LOW = 1
    HIGH = 10

    # Statement that tells you to guess a number in between of low and high
    h1_statement("Guess The Secret Number between {} and {}".format(LOW, HIGH), "*")

    # Generates a secret number
    SECRET = random.randint(LOW, HIGH)
    random = random
    import math

    # Generates amount of guesses based on LOW & HIGH amount
    guesses = HIGH - LOW + 1
    already_guessed = []
    max_raw = math.log2(guesses)
    max_upped = math.ceil(max_raw)
    max_guesses = max_upped + 1
    h1_statement("You have {} Guesses Left".format(max_guesses), "*")
    round_number = 1
    game_stats = []

    GUESSES_ALLOWED = max_guesses

    # Amount of rounds (1 minimum, 5 maximum)
    rounds = int_check("Rounds: ", 1, 5)

    num_won = 0
    rounds_played = 0

    # Loop that checks that you have guesses
    while rounds_played < rounds:
        guess = "1"
        guess_number = 1
        guesses_left = GUESSES_ALLOWED

        # Loop that counts rounds
        while guess != SECRET and guesses_left >= 1:
            h1_statement("│| Round: {} |│".format(round_number), "—")

            # Input guesses
            guess = int_check("Guess ({}): ".format(guess_number), 1, HIGH)
            guess_number += 1
            guesses_left -= 1

            # Checks it's not a duplicate
            if guess in already_guessed:
                h1_statement("You already guessed this number, "
                             "you still have {} guesses".format(guesses_left + 1), "—")
                guesses_left += 1
                guess_number -= 1
                continue

            already_guessed.append(guess)

            # Compares the SECRET to guess (too low/high)
            if guesses_left >= 1:
                if guess < SECRET:
                    h1_statement("Too Low.      │{} Guesses Left│".format(guesses_left), "↑")

                elif guess > SECRET:
                    h1_statement("Too High.     │{} Guesses Left│".format(guesses_left), "↓")

        # If you get SECRET correct
        if guess == SECRET:

            # Guessed in one try
            if guesses_left == GUESSES_ALLOWED - 1:
                h1_statement("Good Job! You got the number in one guess.   **Round Won**", "—")
                num_won += 1
                round_number += 1
                SECRET = random.randint(LOW, HIGH)
                already_guessed = []

            # Guessed in more than 1 try
            else:
                h1_statement("Well Done! You got the number in {} guesses.   **Round Won**".format(
                    GUESSES_ALLOWED - guesses_left), "—")
                num_won += 1
                round_number += 1
                SECRET = random.randint(LOW, HIGH)
                already_guessed = []

        # Prints losing statement
        else:
            h1_statement("You ran out of guesses. The secret was: {}  **Round Lost**".format(SECRET), "—")
            already_guessed = []

            guesses_left -= 1
            round_number += 1
            SECRET = random.randint(LOW, HIGH)

        # End of round info, win/loss counter
        game_stats.append(GUESSES_ALLOWED - guesses_left)
        print("WON: {}      │       LOST: {}\n".format(num_won, rounds_played - num_won + 1))
        rounds_played += 1

    # Game score, scans which round you won/lost
    h1_statement("│| Game Score |│", "—")
    list_count = 1
    for item in game_stats:

        if item > GUESSES_ALLOWED:
            status = "LOST"

        else:
            status = "WON"

        print("Round {}: Guesses: {}  ({})".format(list_count, item, status))
        list_count += 1

    # Game stats
    game_stats.sort()
    best = game_stats[0]
    worst = game_stats[-1]
    average = sum(game_stats) / len(game_stats)

    # Prints game data (round info, best guess, worst guess, average guess per round)
    while rounds_played < rounds:
        print("Round:{}".format(rounds_played + 1))
        rounds_played += 1

    print("\nYou finished your game")
    print()
    print("*** GAME STATISTICS ***")
    print("BEST game: {}".format(best))
    print("WORST game: {}".format(worst))
    print("AVG per game: {:.2f}".format(average))
    print()

    # End of game (Play again or exit)
    keep_going = input("Press <Enter> to continue or any key to quit:")
    print()
print("Thank you for playing this game!!!")
