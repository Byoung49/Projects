# import necesarry libraries
import pandas as pd
import spacy
from spacy.lang.en.examples import sentences 
from spacytextblob.spacytextblob import SpacyTextBlob
# function to remove stop words
def remove_stop_words(sentence):   
  doc = nlp(sentence) 
  filtered_tokens = [token for token in doc if not token.is_stop] 
  return ' '.join([token.text for token in filtered_tokens])
# function to perform sentiment analysis
def sentiment_analysis(review):
    review = review.lower().strip()
    review = remove_stop_words(review)
    doc = nlp(review)
  
    return doc


stop_words = spacy.lang.en.stop_words.STOP_WORDS 

nlp = spacy.load("en_core_web_sm")
nlp.add_pipe('spacytextblob')
# read dataframe.
dataframe = pd.read_csv('amazon_product_reviews.csv', low_memory=False)
# get the review column and clean.
reviews_data = dataframe['reviews.text']
clean_data = dataframe.dropna(subset=['reviews.text'])


s = sentiment_analysis(clean_data['reviews.text'][1])


polarity = s._.blob.polarity
sentiment = s._.blob.sentiment
print(sentiment)


# print statements to show the results.
a = sentiment_analysis(clean_data['reviews.text'][6])
print(a)
b = sentiment_analysis(clean_data['reviews.text'][43])
print(b)
print(a.similarity(b))



