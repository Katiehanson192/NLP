#creating bar charts based on top 10 items and creating word cloud of all items meeting certain criteria

'''
1) Using nyc_trends information, create a bar chart of the top 10 topics based on their corresponding tweet volume.
'''

from turtle import color
from textblob import TextBlob, Word
import nltk 
from pathlib import Path
import pandas as pd

#1) Using nyc_trends information, create a bar chart of the top 10 topics based on their corresponding tweet volume.

from nyc_trends import nyc_trends #brings the dictionary object into the file
from operator import itemgetter

#getting the word and tweet volume into a seperate list
t = nyc_trends[0]['trends']

tweets = []

for i in t: 
    if type(i['tweet_volume']) is int:
        tweets.append((i['name'], i['tweet_volume']))
#print(tweets)

tweets_sorted = sorted(tweets, key = itemgetter(1), reverse= True) #itemgetter(1) = second element in each of the touples
                                                                #this sorts tuples by frequency # in decending order
#print(tweets_sorted)

top_ten_topics = tweets_sorted[:10]
#print(top_ten_topics)

#creating a bar chart

dataframe = pd.DataFrame(top_ten_topics, columns = ['Word', 'Count'])
print()

bar_chart = dataframe.plot.bar(x = 'Word', y = 'Count', legend = False, color= ['mediumvioletred', 'deeppink','navy', 'indigo', 'mediumslateblue', 'steelblue', 'dodgerblue', 
'darkturquoise', 'mediumseagreen', 'lightgreen'])

import matplotlib.pyplot as plt

plt.gcf().tight_layout()
plt.show()

'''
2) Create a Word Cloud of all topics with over 20,000 tweet volume. 
    The size of the word (topic) should be based on their tweet volume.
'''
