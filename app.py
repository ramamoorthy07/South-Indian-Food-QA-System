from flask import Flask, render_template, request, jsonify
import pandas as pd
from sentence_transformers import SentenceTransformer
from sklearn.metrics.pairwise import cosine_similarity
import numpy as np
import re
import llm_manager

# Initialize Flask app
app = Flask(__name__)

# Load the dataset
def load_data(filepath):
    df = pd.read_csv(filepath)
    df['Question'] = df['Question'].str.lower().apply(lambda x: re.sub(r'[^\w\s]', '', x))
    df['Answer'] = df['Answer'].str.strip()
    return df

# Load sentence transformer model and generate embeddings
def generate_embeddings(questions):
    model = SentenceTransformer('all-MiniLM-L6-v2')
    return model, model.encode(questions.tolist())

# Function to process user queries and get answers
def get_answer(user_query, model, question_embeddings, threshold=0.7):
    user_query = re.sub(r'[^\w\s]', '', user_query.lower())
    query_embedding = model.encode([user_query])
    
    similarities = cosine_similarity(query_embedding, question_embeddings)
    max_similarity = np.max(similarities)
    
    if max_similarity >= threshold:
        idx = np.argmax(similarities)
        questions = df['Question'][idx]
        answers = df['Answer'][idx]
        llm_response = llm_manager.get_llm_response_with_context(questions, answers, user_query)
    else:
        llm_response = llm_manager.get_llm_response_without_context(user_query)
   
    return llm_response

# Flask route definitions
@app.route('/')
def index():
    return render_template('index.html')

@app.route('/ask', methods=['POST'])
def ask():
    user_input = request.form['query']
    answer = get_answer(user_input, model, question_embeddings)
    return jsonify({'answer': answer})

if __name__ == '__main__':
    # Load dataset and prepare embeddings
    df = load_data('south_indian_food.csv')
    model, question_embeddings = generate_embeddings(df['Question'])
    
    app.run(debug=True) 