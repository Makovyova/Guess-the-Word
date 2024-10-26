#import re;
import numpy as np;
from navec import Navec;
from gensim.models import KeyedVectors;
path = './navec_hudlit_v1_12B_500K_300d_100q.tar'
navec = Navec.load(path)
#model = KeyedVectors.load(path)

def context_of_words():
    vocab_words = list(navec.vocab.words())  # Use a different variable name if needed
    print(vocab_words[:10])  # Print the first 10 words


def skip_gram(word, navec, top_n=5):
    word='живое'
    try:
        # Get the most similar words
        similar_words = navec.most_similar(word, topn=top_n)
        # Extract the words from the tuples returned
        return [similar_word for similar_word, _ in similar_words]
    except KeyError:
        print(f"The word '{word}' is not in the vocabulary.")
        return []
