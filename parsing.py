import nltk
from nltk.grammar import CFG

# Define the sentence and its corresponding CFG grammar
sentence = "The powerful party can hold the majority"
grammar = CFG.fromstring("""
    S -> NP VP
    NP -> Det Adj N | Det N
    VP -> V NP | V Det N
    Det -> 'The'| 'the'
    Adj -> 'powerful'
    N -> 'party' | 'majority'
    V -> 'can' | 'hold'
""")

# Function for chart parsing and printing parse trees
def chart_parsing_with_trees(sentence, grammar):
    # Create a ChartParser using the given grammar
    parser = nltk.ChartParser(grammar)
    
    # Tokenize the input sentence
    tokens = nltk.word_tokenize(sentence)
    
    # Parse the tokens using the ChartParser
    chart = parser.chart_parse(tokens)
    
    # Print the edges of the chart
    for edge in chart.edges():
        print(edge)
    
    # Parse the tokens and print parse trees
    for tree in parser.parse(tokens):
        # Print the parse tree
        print(tree)
    
    print("done")

# Perform chart parsing and print parse trees for the given sentence
chart_parsing_with_trees(sentence, grammar)

