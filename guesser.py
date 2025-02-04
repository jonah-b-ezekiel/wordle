import sys
import pickle
from utils.helpers import get_guesses, get_answers, get_feedback_lookup, get_partition_map, update_answers

def get_guess(
    guesses: list[str],
    answers: list[str],
    feedback_lookup: dict[str, dict[str, str]],
    partition_map: dict[str, dict[str, set[str]]],
    guess_number: int,
) -> str:
    """
    Determines the next best guess for the Wordle solver.

    Parameters:
    ----------
    guesses : list[str]
        A list of all possible guesses. These can include both valid answers and other guessable words.
    answers : list[str]
        A list of remaining valid answers based on previous feedback. Initially, this contains all possible answers.
    feedback_lookup : dict[str, dict[str, str]]
        A precomputed dictionary mapping (guess, answer) pairs to their corresponding feedback.
        - Outer dict: Maps a guess (str) to an inner dict.
        - Inner dict: Maps an answer (str) to a feedback string (e.g., "ggbby").
        - Feedback indicates which letters are correct ("g"), present but misplaced ("y"), or absent ("b").
    partition_map : dict[str, dict[str, set[str]]]
        A precomputed dictionary mapping each guess to a partition of possible answers by feedback.
        - Outer dict: Maps a guess (str) to an inner dict.
        - Inner dict: Maps feedback strings (str) to sets of possible answers (set[str]).
        - Helps evaluate how well a guess partitions the remaining answers.
    guess_number : int
        
    Returns:
    -------
    str
        The next best guess based on the current state of the solver.

    Usage:
    ------
    To implement your own `get_guess` logic:
    1. Use `partition_map` to determine how well each guess splits the remaining answers.
       Example: For a guess, use `partition_map[guess]` to access the dictionary of feedback → set of answers.
    2. Use `feedback_lookup` to quickly retrieve feedback for a (guess, answer) pair.
       Example: `feedback_lookup[guess][answer]` gives the feedback string for that pair.
    3. Choose a strategy, such as minimizing the average size of partitions, maximizing information gain, or prioritizing guesses that are still valid answers.

    Example Implementation:
    ------------------------
    # Iterate over all guesses and evaluate their effectiveness:
    for guess in guesses:
        total_partition_size = 0
        for answer in answers:
            feedback = feedback_lookup[guess][answer]
            total_partition_size += len(partition_map[guess][feedback])
        # Use total_partition_size to rank guesses and decide the best guess.
    """
    if len(answers) == 2309:  # Recommended initial guess to speed up testing.
        return 'roate'  # Replace with your preferred starting guess.
    return next(iter(answers))  # Return random remaining possible answer