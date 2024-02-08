from textblob import TextBlob
from newspaper import Article
url = 'https://www.hindustantimes.com/entertainment/bollywood/poonam-pandey-fake-death-celebs-react-101706945987655.html'
article = Article(url)
article.download()
article.parse()
article.nlp()
text = article.text
text = article.summary
print(text)
blob = TextBlob(text)
sentiment = blob.sentiment.polarity
print(sentiment)