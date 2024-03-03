from textblob import TextBlob
from textblob.sentiments import NaiveBayesAnalyzer
from newspaper import Article

url = 'https://timesofindia.indiatimes.com/city/chennai/where-theres-a-well-theres-a-way/articleshow/103824570.cms'

article = Article(url)
article.download()
article.parse()
article.nlp()
text = article.text
summary = article.summary
print(summary)

# Analyze sentiment using Naive Bayes analyzer
blob = TextBlob(text, analyzer=NaiveBayesAnalyzer())
classification = blob.sentiment.classification
positive_prob = blob.sentiment.p_pos
negative_prob = blob.sentiment.p_neg

print("\n\nSentiment:", classification)

