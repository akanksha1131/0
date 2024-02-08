import nltk
from nltk.tokenize import word_tokenize, sent_tokenize
from nltk.tag import pos_tag
text = "Time to get started with natural language processing!"
word_tokens = word_tokenize(text)
tags = pos_tag(word_tokens)
print(tags)
