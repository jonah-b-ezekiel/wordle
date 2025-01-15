from utils.helpers import get_answers, get_guesses, get_feedback_lookup, get_partition_map, update_answers
from guesser import get_guess

def main():
    print("Starting Wordle Solver Testing...")
    
    feedback_lookup = get_feedback_lookup()
    partition_map = get_partition_map()
    guesses = get_guesses()
    answers = get_answers()

    total_answers = len(answers)
    result = 0

    for idx, answer in enumerate(answers):
        progress = (idx + 1) / total_answers * 100
        print(f"Progress: {progress:.2f}% ({idx + 1}/{total_answers})", end="\r")

        answers_copy = answers.copy()
        for num_guesses in range(1, 10):
            guess = get_guess(guesses, answers_copy, feedback_lookup, partition_map)
            feedback = feedback_lookup[guess][answer]

            if feedback == 'ggggg':
                result += num_guesses
                break

            update_answers(guess, feedback, answers_copy, partition_map)

    average_guesses = result / total_answers
    print("\nTesting complete!")
    print(f"Average number of guesses: {average_guesses:.2f}")

if __name__ == "__main__":
    main()