import tweepy
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from wordcloud import WordCloud
from textblob import TextBlob
import folium
import geopandas
import geopy
import numpy as np
import os
import re 

def plot_cloud(word_cloud):
    plt.figure(figsize=(40,30))
    plt.imshow(word_cloud)
    word_cloud.to_file('hp_cloud_simple.png')
    plt.axis('off')


require_col = [i for i in range(12)]
datasheet = pd.read_excel('twitterDataset.xlsx', usecols=require_col)


# Create a pandas DataFrame to store the tweets
df = pd.DataFrame(data=[text for text in datasheet['text']], columns=['Tweets'])

# Add additional columns for the tweet attributes
df['len'] = np.array([len(text) for text in datasheet['text']])
df['date'] = np.array([date for date in datasheet['date']])
df['source'] = np.array([source for source in datasheet['source']])
df['likes'] = np.array([fav for fav in datasheet['user_favourites']])

# I) Trending topic
# Identify the most common hashtags in the tweets  

hashtags = []
for hashtag in datasheet['hashtags']:
    try:
        tmp = hashtag.replace('[', '').replace(']', '').replace("'", '').replace(',', '').split(' ')

        for hashtg in tmp:
            hashtags.append(hashtg)
    except:
        continue   

hashtag_freq = pd.Series(hashtags).value_counts()
print(hashtag_freq)

# II) Word cloud
# Create a word cloud based on the text of the tweets
text = " ".join([text for text in datasheet['text']])
wordcloud = WordCloud().generate(text)  

plot_cloud(wordcloud)

# III) Sentiment analysis
# Calculate the sentiment score of each tweet
df['sentiment'] = np.array([TextBlob(tweet).sentiment.polarity for tweet in df['Tweets']])

# IV) Visualize the tweets on the map
# Create a map of the specified location
m = folium.Map(location=[45.5236, -122.6750], zoom_start=13)

locator = geopy.geocoders.Nominatim(user_agent="myGeocoder")


# Add markers for the tweets to the map
# for tweet in datasheet['user_location']:
#     if tweet != '':
#         folium.Marker((location.latitude, location.longitude), popup='test').add_to(m)

print(df['sentiment'])