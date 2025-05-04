from flask import Flask, render_template, request
import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
import re

app = Flask(__name__)

df = pd.read_csv("dataset.csv")
df.dropna(inplace=True)

def clean_text(text):
    text = text.lower()
    text = re.sub(r"[^a-z0-9\\s]", "", text)
    return text.strip()

df['clean_question'] = df['question'].apply(clean_text)
questions = df['clean_question'].tolist()
answers = df['answer'].tolist()

vectorizer = TfidfVectorizer()
X = vectorizer.fit_transform(questions)

def get_answer(user_input):
    user_input_clean = clean_text(user_input)
    user_vec = vectorizer.transform([user_input_clean])
    similarity = cosine_similarity(user_vec, X)
    idx = similarity.argmax()
    confidence = similarity[0][idx]
    if confidence > 0.4:
        return answers[idx]
    else:
        return "Sorry, I don't understand the question."

@app.route('/')
def index():
    return render_template("index.html")

@app.route('/chat', methods=['POST'])
def chat():
    user_question = request.form['question']
    answer = get_answer(user_question)
    return render_template("index.html", question=user_question, answer=answer)

if __name__ == '__main__':
    app.run(debug=True)
