from gensim.models import Word2Vec
from nltk.tokenize import sent_tokenize, word_tokenize
import nltk

# Download punkt for tokenization
nltk.download('punkt')

# Sample text data
text = "Word2Vec is a technique to create word embeddings. It is very useful for NLP tasks."

# Tokenize the text into sentences and words
sentences = sent_tokenize(text)
tokenized_sentences = [word_tokenize(sentence.lower()) for sentence in sentences]

# Train the Word2Vec model
model = Word2Vec(sentences=tokenized_sentences, vector_size=100, window=5, min_count=1, workers=4)

# Save the model
model.save("word2vec.model")

# Load the model
model = Word2Vec.load("word2vec.model")

# Find the vector of a word
word_vector = model.wv['word2vec']
print("Vector representation of 'word2vec':\n", word_vector)

# Find most similar words
similar_words = model.wv.most_similar('word2vec', topn=5)
print("Most similar words to 'word2vec':\n", similar_words)
