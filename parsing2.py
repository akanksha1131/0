import nltk
from nltk.grammar import CFG
from nltk.app.chartparser_app import ChartParserApp

# Define the sentence and its corresponding CFG grammar
sentence = "The powerful party can hold the majority"
grammar = CFG.fromstring("""
    S -> NP VP
    NP -> ART ADJ N
    NP -> ART N
    NP -> ADJ N  
    VP -> V VP
    VP -> V NP               
    ART -> 'The'| 'the'
    ADJ -> 'powerful'
    N -> 'party' | 'majority'
    V -> 'can' | 'hold'
    

""")

# Tokenize the input sentence
tokens = nltk.word_tokenize(sentence)

# Create a ChartParser using the given grammar
parser = nltk.ChartParser(grammar)

# Create and run the ChartParserApp
chart_parser_app = ChartParserApp(parser, tokens)
chart_parser_app.mainloop()
