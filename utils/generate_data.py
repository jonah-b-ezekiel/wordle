import os
import pickle
from collections import defaultdict
from helpers import get_answers, get_guesses, get_feedback

data_dir = os.path.join(os.path.dirname(__file__), '..', 'data')

guesses = get_guesses()
answers = get_answers()

feedback_lookup = {}
for guess in guesses:
    feedback_lookup[guess] = {}
    for answer in answers:
        feedback_lookup[guess][answer] = get_feedback(guess, answer)

partition_map = {}
for guess in guesses:
    feedback_to_answers = defaultdict(set)
    for answer in answers:
        feedback = feedback_lookup[guess][answer]
        feedback_to_answers[feedback].add(answer)
    partition_map[guess] = dict(feedback_to_answers)


with open(os.path.join(data_dir, 'feedback_lookup.pkl'), 'wb') as f:
    pickle.dump(feedback_lookup, f)

with open(os.path.join(data_dir, 'partition_map.pkl'), 'wb') as f:
    pickle.dump(partition_map, f)