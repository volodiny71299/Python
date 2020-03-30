def h1_statement(statement, char):
    # print()
    print(char * len(statement))
    print(statement)
    print(char * len(statement))
    print()


# minimum = 0.99


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


keep_going = ""
while keep_going == "":

    import random

    LOW = 1
    HIGH = 10

    h1_statement("Guess The Secret Number between {} and {}".format(LOW, HIGH), "*")

    SECRET = random.randint(LOW, HIGH)
    random = random
    import math

    guesses = HIGH - LOW + 1
    already_guessed = []
    max_raw = math.log2(guesses)
    max_upped = math.ceil(max_raw)
    max_guesses = max_upped + 1
    h1_statement("You have {} guesses left".format(max_guesses), "*")
    round_number = 1
    game_stats = []

    GUESSES_ALLOWED = max_guesses

    rounds = int_check("Rounds: ", 1, 5)

    num_won = 0
    rounds_played = 0

    while rounds_played < rounds:
        guess = "1"
        guess_number = 1
        guesses_left = GUESSES_ALLOWED

        while guess != SECRET and guesses_left >= 1:
            h1_statement("│| Round: {} |│".format(round_number), "—")
            guess = int_check("Guess ({}): ".format(guess_number), 1, HIGH)
            guess_number += 1
            guesses_left -= 1

            if guess in already_guessed:
                h1_statement("You already guessed this number, "
                             "you still have {} guesses".format(guesses_left + 1), "—")
                guesses_left += 1
                guess_number -= 1
                continue

            already_guessed.append(guess)

            if guesses_left >= 1:
                if guess < SECRET:
                    h1_statement("Too Low.      │{} guesses left│".format(guesses_left), "↑")

                elif guess > SECRET:
                    h1_statement("Too High.     │{} guesses left│".format(guesses_left), "↓")

        if guess == SECRET:
            if guesses_left == GUESSES_ALLOWED - 1:
                h1_statement("Good Job! You got the number in one guess.   **Round Won**", "—")
                num_won += 1
                round_number += 1
                SECRET = random.randint(LOW, HIGH)
                already_guessed = []

            else:
                h1_statement("Well Done! You got the number in {} guesses.   **Round Won**".format(
                    GUESSES_ALLOWED - guesses_left), "—")
                num_won += 1
                round_number += 1
                SECRET = random.randint(LOW, HIGH)
                already_guessed = []

        else:
            h1_statement("You ran out of guesses.  **Round Lost**", "—")
            already_guessed = []

            guesses_left -= 1
            round_number += 1
            SECRET = random.randint(LOW, HIGH)

        game_stats.append(GUESSES_ALLOWED - guesses_left)
        print("WON: {}      │       LOST: {}\n".format(num_won, rounds_played - num_won + 1))
        rounds_played += 1

    h1_statement("│| Game Score |│", "—")
    list_count = 1
    for item in game_stats:

        if item > GUESSES_ALLOWED:
            status = "LOST"

        else:
            status = "WON"

        print("Round {}: Guesses: {}  ({})".format(list_count, item, status))
        list_count += 1

    game_stats.sort()
    best = game_stats[0]
    worst = game_stats[-1]
    average = sum(game_stats) / len(game_stats)

    while rounds_played < rounds:
        print("Round:{}".format(rounds_played + 1))
        rounds_played += 1

    print("You finished your game")
    print()
    print("*** GAME STATISTICS ***")
    print("BEST: {}".format(best))
    print("WORST: {}".format(worst))
    print("AVERAGE: {:.2f}".format(average))

    print()
    keep_going = input("Press <Enter> to continue or any key to quit:")
    print()
print("Thank you for playing this game!!!")
