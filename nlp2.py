from textblob import TextBlob
import nltk 
from pathlib import Path
import pandas as pd


#eliminate stop words when analyzing code (ex: the, and, etc.-look at powerpoint for list of words
#stopwords = a list, so you can add to it

#nltk.download("stopwords")
from nltk.corpus import stopwords

stops = stopwords.words("english")
#print(stops) #prints out the list of "stop words" - these are the words that you may not want to be considered while doing text analysis

blob = TextBlob("Today is a beautiful day.")  #textblob = puts words into a list

#print(blob.words) 
'''
cleanlist = []
for words in blob.words: #how to create a new list of words that don't include any of the words in stop words
    if words not in stops:
        cleanlist.append(words)
print(cleanlist)
'''

cleanlist = [word for word in blob.words if word not in stops]
#print(cleanlist)

blob = TextBlob(Path("RomeoAndJuliet.txt").read_text())  


#print(blob.word_counts["juliet"])

#print(blob.noun_phrases.count("lady capulet"))

more_stops = ["thee", "thy", "thou"]

stops +=more_stops

items = blob.word_counts.items()
#print(items) #this counts how many times each word is used, returns as a tuple

#use a list comprehension to eliminate any tuples containing stop words
items = [i for i in items if i [0] not in stops] #i[0] = first element of the tuple as it cycles through. checks to see if the word is in the stops list or not
print(items[:10])

from operator import itemgetter
sorted_items = sorted(items)
print(sorted_items[:10]) #this sorts words alphabetically

sorted_items = sorted(items, key = itemgetter(1), reverse= True) #itemgetter(1) = second element in each of the touples
                                                                #this sorts tuples by frequency # in decending order
print(sorted_items[:10])

top20 = sorted_items[:20]

df = pd.DataFrame(top20, columns= ["Word", "Count"]) #creates a dataframe for the top 20 results
print(df)

import matplotlib as plt
df.plot.bar(x= "Word", y="Count", legend= False)

plt.gcf().tight_layout() #need to fix this???

plt.show()