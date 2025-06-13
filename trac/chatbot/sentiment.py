import nltk
from nltk.sentiment.vader import SentimentIntensityAnalyzer

class Feelings:
    def __init__(self):
        nltk.download("vader_lexicon")
        self.analyzer = SentimentIntensityAnalyzer()

    def classify(self, text):
        compound = self.analyzer.polarity_scores(text)['compound']
        if compound < -0.5:
            return "negative"
        elif compound > 0.5:
            return "positive"
        else:
            return "neutral"