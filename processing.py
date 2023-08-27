import requests
from bs4 import BeautifulSoup
import nltk
import string
from nltk.corpus import stopwords

nintendo_wiki = 'https://en.wikipedia.org/wiki/Nintendo'
page = requests.get(nintendo_wiki)

soup = BeautifulSoup(page.text, 'html.parser')

### EXTRACTS THE TEXT FROM THE WEBSITE
text = soup.get_text()

### MAKES ALL OF THE TEXT LOWERCASE TO MAKE SURE THERE ARE NO REPETITIONS
clean_text = text.lower()

### MAKING A TRANSLATION TABLE AND THEN USING IT TO REMOVE ALL OF THE PUNCTUATION
table = str.maketrans('', '', string.punctuation)
clean_text = clean_text.translate(table)

### PERFORMS WORD-LEVEL TOKENIZATION
words = clean_text.split()

clean_words = []

### LOOPING THROUGH EVERY WORD AND ONLY APPENDING IF IT IS NOT A STOP WORD
for token in words:
    if token not in stopwords.words('english'):
        clean_words.append(token)

### CHECKS THE FREQUENCY OF THE WORDS
freq = nltk.FreqDist(clean_words)

### PLOTS THE 20 MOST USED WORDS
freq.plot(20, title = 'Frequency Distribution')