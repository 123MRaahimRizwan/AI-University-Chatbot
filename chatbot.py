# chatbot.py
import pickle
import numpy as np
from sentence_transformers import SentenceTransformer
import google.generativeai as genai

# Load chunks and embeddings
with open("chunks.pkl", "rb") as f:
    chunks, embeddings = pickle.load(f)

# Load embedding model
embedder = SentenceTransformer("all-MiniLM-L6-v2")

# Gemini config
genai.configure(api_key="AIzaSyAJx29bCioUOBP7tjP9t7Nmjuxu3d3dyAg")
model = genai.GenerativeModel("gemini-2.0-flash")

def get_response(user_query):
    query_embedding = embedder.encode([user_query])[0]
    similarities = np.dot(embeddings, query_embedding)
    
    # Get top 3 matches
    top_indices = np.argsort(similarities)[-3:][::-1]
    top_chunks = [chunks[i]['text'] for i in top_indices]

    context = "\n\n".join(top_chunks)

    prompt = f"""You are a helpful university assistant. Use the following information from official university documents to answer the question truthfully:

{context}

Question: {user_query}
Answer:"""

    response = model.generate_content(prompt)
    return response.text



# API KEY = AIzaSyBZE1JEguMawQWXghb7sG18lCtb