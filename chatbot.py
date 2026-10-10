"""
Chatbot engine.
Step 2: preprocess text with NLTK (clean, tokenize, remove stopwords, lemmatize)
Step 3: match the user question to the most similar FAQ (TF-IDF + cosine similarity)
Step 4: display the best matching answer

Run in terminal:  python chatbot.py
"""

import re

import nltk
from nltk.corpus import stopwords
from nltk.stem import WordNetLemmatizer
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

from faqs import FAQS

# One-time downloads of NLTK data (needs internet the first time)
for pkg in ("punkt", "punkt_tab", "stopwords", "wordnet", "omw-1.4"):
    nltk.download(pkg, quiet=True)

lemmatizer = WordNetLemmatizer()
stop_words = set(stopwords.words("english"))
THRESHOLD = 0.25


def preprocess(text):
    text = re.sub(r"[^a-z\s]", "", text.lower())
    tokens = nltk.word_tokenize(text)
    return " ".join(lemmatizer.lemmatize(t) for t in tokens if t not in stop_words)


questions = [q for q, _ in FAQS]
answers = [a for _, a in FAQS]
vectorizer = TfidfVectorizer()
question_vectors = vectorizer.fit_transform([preprocess(q) for q in questions])


def get_answer(user_text):
    query_vector = vectorizer.transform([preprocess(user_text)])
    scores = cosine_similarity(query_vector, question_vectors)[0]
    best = scores.argmax()
    if scores[best] < THRESHOLD:
        return "Sorry, I couldn't find an answer to that. Could you rephrase your question?"
    return answers[best]


if __name__ == "__main__":
    print("FAQ Chatbot - type 'quit' to exit\n")
    while True:
        text = input("You: ").strip()
        if text.lower() in ("quit", "exit"):
            break
        print("Bot:", get_answer(text), "\n")
        