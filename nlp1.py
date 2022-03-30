from textblob import TextBlob, Word
#uses default analyzer

text = "Today is a beautiful day. Tomorrow looks like bad weather."

blob = TextBlob(text)

#print(blob)

sentences = blob.sentences #creates a sentence object, puts sentences in a list so their interable

#print(sentences)

words = blob.words

#print(words)

#print(blob.tags) #list of each word + corresponding part of speech (ex: noun, verb, etc.)
                 #nn = noun, vbz = verb,JJ = adjective, DT = determinate, NNP = Proper Singular Noun, IN = subordinating conjunction

#print(blob.noun_phrases)
'''
#Sentence Sentiment analysis (is sentence positive or negative)
print(blob.sentiment) #privides polarity - how positive or negative something is, and how subjective something is
                     #both range from -1 to 1?

print(blob.sentiment.polarity)
print(blob.sentiment.subjectivity)

#display polarity of each sentence
for i in sentences:
    print(f' polarity for the sentence "{i}" is: {round(i.sentiment.polarity,3)}')
    #print(round(i.sentiment.polarity,3))
'''
'''
from textblob.sentiments import NaiveBayesAnalyzer
#changing from default analyzer

blob = TextBlob(text, analyzer = NaiveBayesAnalyzer())
sentences = blob.sentences

print(blob.sentiment) #compare if positive and negative is higher

for i in sentences:
    print(f' sentiment for the sentence "{i}" is: {i.sentiment}') #can't use round() on this??
'''

'''
#this is translated from Google translate
spanish = blob.translate(to = "es")
print(spanish)

chinese = blob.translate(to = "zh")
print(chinese)

french = blob.translate(to = "fr")
print(french)

hindi = blob.translate(to = 'ne')
print(hindi)

english = hindi.translate()
print(english)
'''
'''
from textblob import Word

index = Word('index') #plural form of the word
cacti = Word('cacti') #makes this singular

print(index.pluralize())
print(cacti.singularize())

#wordlist
animals = TextBlob('dog cat fish bird').words
print(animals.pluralize())

#spellcheck and corrections
word = Word('theyr')
print(word.spellcheck()) #returns confidence level of what python thinks the user was trying to spell
print(word.correct()) #picks the spellcheck word with the highest confidence 
'''
'''
#Steming 
    #steming = takes out end of the words?
from nltk.stem import WordNetLemmatizer

word1 = Word('Studies')
word2 = Word('varieties')

print(word1.stem())
print(word2.stem())

print(word1.lemmatize())
print(word2.lemmatize())
'''

#syn and ant
happy = Word('happy')

print(happy.definitions)
print(happy.synsets)
