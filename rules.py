from itertools import product
from nltk.grammar import CFG

# Define the sentence
sentence = "The powerful party can hold the majority"

# Define all possible parts of speech for each word in the sentence
parts_of_speech = {
    'The': ['Det'],
    'the': ['Det'],
    'powerful': ['Adj'],
    'party': ['N'],
    'can': ['V'],
    'win': ['V'],
    'election': ['N']
}

# Generate all possible combinations of parts of speech
possible_combinations = list(product(*[parts_of_speech[word] for word in sentence.split()]))

# Generate CFG grammar rules without duplication
grammar_rules = set()
for combination in possible_combinations:
    rules = [f"{pos} -> '{word}'" for word, pos in zip(sentence.split(), combination)]
    grammar_rules.add('\n'.join(rules))

# Join all grammar rules into a single string
grammar_string = '\n'.join(grammar_rules)

# Create CFG object from the grammar string
grammar = CFG.fromstring(grammar_string)

# Print the grammar rules
print(grammar)