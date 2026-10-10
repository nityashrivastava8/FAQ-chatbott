# FAQ Chatbot

A chatbot that answers frequently asked questions. It was built for Task 2 of the CodeAlpha AI Internship.

## Demo

[Watch the demo video here](demo.mp4)

## How it works

1. **Collect FAQs:** questions and answers are stored in `faqs.py`.
2. **Preprocess text:** NLTK cleans the text (lowercase, tokenize, remove stopwords, lemmatize).
3. **Match questions:** TF-IDF vectors and cosine similarity find the most similar FAQ.
4. **Display the answer:** the best matching answer is returned as the chatbot reply.
5. **Chat UI:** a simple chat window built with Flask, HTML and JavaScript.

## Tech used

Python, NLTK, scikit-learn, Flask, HTML/CSS/JavaScript

## Files

| File | Purpose |
|------|---------|
| `faqs.py` | FAQ questions and answers |
| `chatbot.py` | Text preprocessing and matching (also runs in the terminal) |
| `app.py` | Flask server for the chat window |
| `chat.html` | Chat window page |
| `requirements.txt` | Python packages needed |

## How to run

```
python -m venv venv
venv\Scripts\activate
pip install -r requirements.txt
python app.py
```

Then open http://127.0.0.1:5000 in your browser.

To test in the terminal instead, run `python chatbot.py`.

## Screenshots

[<video controls src="chatbot.py - faq chatbot - Visual Studio Code 2026-10-10 17-55-22.mp4" title="Title"></video>]
