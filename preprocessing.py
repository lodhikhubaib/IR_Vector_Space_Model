import tkinter as tk
import nltk
import string
import re
import os
import csv
import pickle
from collections import defaultdict
from nltk.tokenize import word_tokenize
from nltk.stem import PorterStemmer
from nltk.stem import WordNetLemmatizer
nltk.download("wordnet")
nltk.download("omw-1.4")
nltk.download('punkt')

# Function to remove URLs from text
def removing_url(text):
    url_pattern = re.compile(r'https?://\S+|http?://\S+|http\.\S+|www\.\S+')
    return url_pattern.sub(' ', text)

# Tokenization function
def tokenization(content_Without_URL):
    #removing numbers from the word that combine together Like this 1faculty
    content_Without_URL = content_Without_URL.replace("1", " ")
    content_Without_URL = content_Without_URL.replace("2", " ") 
    content_Without_URL = content_Without_URL.replace("3", " ")
    content_Without_URL = content_Without_URL.replace("4", " ")
    content_Without_URL = content_Without_URL.replace("5", " ")
    content_Without_URL = content_Without_URL.replace("6", " ")
    content_Without_URL = content_Without_URL.replace("7", " ")
    content_Without_URL = content_Without_URL.replace("8", " ")
    content_Without_URL = content_Without_URL.replace("9", " ")
    content_Without_URL = content_Without_URL.replace("0", " ")
    content_Without_URL = content_Without_URL.replace("�", " ")
    content_Without_URL = content_Without_URL.replace("", " ")
    content_Without_URL = content_Without_URL.replace("¨", " ")
    content_Without_URL = content_Without_URL.replace("´", " ")
    content_Without_URL = content_Without_URL.replace("¼", " ")
    content_Without_URL = content_Without_URL.replace("¸", " ")
    content_Without_URL = content_Without_URL.replace("···", " ")
    content_Without_URL = content_Without_URL.replace("·", " ")
    content_Without_URL = content_Without_URL.replace("······", " ")
    content_Without_URL = content_Without_URL.replace("×", " ")
    content_Without_URL = content_Without_URL.replace("ß", " ")
    content_Without_URL = content_Without_URL.replace("ü", " ")
    content_Without_URL = content_Without_URL.replace("þ", " ")
    content_Without_URL = content_Without_URL.replace("˜", " ")
    content_Without_URL = content_Without_URL.replace("š", " ")
    content_Without_URL = content_Without_URL.replace("ž", " ")
    content_Without_URL = content_Without_URL.replace("ý", " ")
    content_Without_URL = content_Without_URL.replace("ˆ", " ")
    content_Without_URL = content_Without_URL.replace("–", " ")
    content_Without_URL = content_Without_URL.replace("•", " ")
    content_Without_URL = content_Without_URL.replace("…", " ")
    content_Without_URL = content_Without_URL.replace("——", " ")
    content_Without_URL = content_Without_URL.replace("—", " ")
    # Tokenize the content into words
    words = word_tokenize(content_Without_URL)
    return words

# Function to process a file
def process_file(file_path):
    with open(file_path, "r") as file:
        content = file.read()
        content_Without_URL = removing_url(content)
    words = tokenization(content_Without_URL)
    normalized_words = normalization(words)
    return normalized_words

# Function to remove punctuation and special characters from each word and filter out empty strings
def removing_punctuation(words):
    table = str.maketrans('', '', string.punctuation + '�')
    return [word.translate(table) for word in words if word.translate(table)]

# Load stop words from Stopword-List.txt
with open("Stopword-List.txt","r") as file:
    stopwords = file.read().split()

# Function to remove stop words from the tokens
def remove_stop_words(words):
    return [token for token in words if token.lower() not in stopwords]

# Function to remove numbers and single character tokens from the tokens
def remove_single_character_tokens(words):
    return [token for token in words if not token.isdigit() and len(token) > 1 ]

# Case Folding: Making the Tokens into Small letters
def case_fold(tokens):
    return [token.lower() for token in tokens]
# Function to normalize the tokens
def normalization(tokens):
    tokens = removing_punctuation(tokens)
    tokens = remove_stop_words(tokens)
    tokens = remove_single_character_tokens(tokens)
    tokens = case_fold(tokens)
    tokens = stemming(tokens)  # Fix: Defined the stemming function before using it
    #tokens = lemmatization(tokens)
    return tokens

# Stemming function: To make the Tokens into Root form. Like classification into classifi
def stemming(words):
    ps = PorterStemmer()
    stemmed_word = []
    for w in words:
        stemmed_word.append(ps.stem(w))
    return stemmed_word


#lemmatization
def lemmatization(words):
    wnl = WordNetLemmatizer()
    lemmatized_words = []
    for w in words:
        lemma_word = wnl.lemmatize(w)
        lemmatized_words.append(lemma_word)
    return lemmatized_words