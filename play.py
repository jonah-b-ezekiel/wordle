from utils.helpers import get_answers, get_feedback_lookup, get_guesses, get_partition_map, update_answers
from guesser import get_guess

def main():
    print("Welcome to the Wordle Solver!")
    print("Instructions:")
    print("1. Input your guess when prompted.")
    print("2. Input feedback as a string of five characters using:")
    print("   - 'g' for green (correct letter in the correct position).")
    print("   - 'y' for yellow (correct letter in the wrong position).")
    print("   - 'b' for black (incorrect letter).")
    print("Type 'exit' anytime to quit the solver.")
    print()

    feedback_lookup = get_feedback_lookup()
    partition_map = get_partition_map()
    answers = get_answers()
    guesses = get_guesses()
    guess_number = 0
    while True:
        guess_number += 1
        suggested_guess = get_guess(guesses, answers, feedback_lookup, partition_map, guess_number)
        print(f"\nSuggested guess: {suggested_guess} (Remaining answers: {len(answers)})")

        guess = input("Please input your guess (or type 'exit' to quit): ").strip().lower()
        if guess == "exit":
            print("Exiting Wordle Solver. Goodbye!")
            break

        feedback = input("Please input feedback (e.g., 'gybbg'): ").strip().lower()
        if feedback == "exit":
            print("Exiting Wordle Solver. Goodbye!")
            break

        if len(feedback) != 5 or not all(c in "gyb" for c in feedback):
            print("Invalid feedback! Please use 'g', 'y', and 'b' only, and ensure it is 5 characters long.")
            continue

        update_answers(guess, feedback, answers, partition_map)

        if len(answers) == 1:
            print(f"\nThe answer is: {list(answers)[0]}. Congratulations!")
            break

if __name__ == "__main__":
    main()