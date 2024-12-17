import nltk
import spacy
import subprocess
from nltk.corpus import stopwords
from nltk.util import ngrams
from nltk.tokenize import word_tokenize
import pickle
import pandas as pd


def preprocess_docs(document):
    # NLTK
    try:
        nltk.data.find('corpora/stopwords')
    except LookupError:
        nltk.download('stopwords')
    # Spacy
    try: 
        nlp_spacy = spacy.load('en_core_web_sm')
    except OSError:
        print('Spacy model not found. Downloading now.')
        subprocess.run(['python', '-m', 'spacy', 'download', 'en_core_web_sm'], check=True)
        nlp_spacy = spacy.load('en_core_web_sm')
        
    lemmatized_doc = ' '.join([token.lemma_ for token in nlp_spacy(document)])
    token_filter_alnum = [token for token in word_tokenize(lemmatized_doc.lower()) if token.isalnum()]
    stop_words = set(stopwords.words('english'))
    token_filter_stop_words = [token for token in token_filter_alnum if token not in stop_words]
    processed_document = ' '.join(token_filter_stop_words)

    return processed_document


def preprocess_pipe(document):
    doc = preprocess_docs(document)
    with open('./model/count_vectorizer.pkl', 'rb') as f:
        count_vec = pickle.load(f)
    doc_tfidf = count_vec.transform([doc])
    return doc_tfidf
