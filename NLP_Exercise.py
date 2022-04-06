#creating bar charts based on top 10 items and creating word cloud of all items meeting certain criteria

'''
1) Using nyc_trends information, create a bar chart of the top 10 topics based on their corresponding tweet volume.
'''

from turtle import color
from textblob import TextBlob, Word
import nltk 
from pathlib import Path
import pandas as pd
from wordcloud import WordCloud
import imageio

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
#tweets_sorted = all tweets sorted based on highest number

tweets_dict = dict(tweets_sorted)

over_20000 = []

for value in tweets_dict:
    if tweets_dict[value] > 20000:
        over_20000.append((value, tweets_dict[value]))
#print(type(over_20000))

#making the word cloud
mask_image = imageio.imread('twitter_mask1.png')

wordcloud = WordCloud(colormap='RdYlBu', mask = mask_image,  background_color='white', contour_width = 3, contour_color='black') #Why isn't there a color map that better matches the NY colors???

over_20000 = str(over_20000)

wordcloud = wordcloud.generate(over_20000)

wordcloud = wordcloud.to_file('NYC_Twitter_Trends_WordCloud.png')
plt.imshow(wordcloud)

