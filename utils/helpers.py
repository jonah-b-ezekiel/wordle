import pickle

def get_guesses():
    with open('data/guesses.txt', 'r', encoding='utf-8') as file:
        content = file.read()
    words = content.split()
    return set(words) | get_answers()

def get_answers():
    with open('data/answers.txt', 'r', encoding='utf-8') as file:
        content = file.read()
    words = content.split()
    return set(words)

def get_feedback_lookup():
    with open('data/feedback_lookup.pkl', 'rb') as f:
        return pickle.load(f)
    
def get_partition_map():
    with open('data/partition_map.pkl', 'rb') as f:
        return pickle.load(f)
    
def update_answers(guess, feedback, answers, partition_map):
    valid = partition_map[guess].get(feedback, set())
    answers.intersection_update(valid)

def get_feedback(guess, answer):
    answer_remaining = list(answer)
    result = ['b'] * 5 

    for i in range(5):
        if guess[i] == answer[i]:
            result[i] = 'g' 
            answer_remaining[i] = None  

    for i in range(5):
        if result[i] == 'b' and guess[i] in answer_remaining:
            result[i] = 'y' 
            index_to_remove = answer_remaining.index(guess[i])
            answer_remaining[index_to_remove] = None

    return ''.join(result)