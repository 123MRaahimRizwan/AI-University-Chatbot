# pdf_ingestion.py

import os
import pickle
from PyPDF2 import PdfReader
from langchain.text_splitter import RecursiveCharacterTextSplitter
from sentence_transformers import SentenceTransformer

# Step 1: Read all PDFs
all_texts = []

for filename in os.listdir("data"):
    if filename.endswith(".pdf"):
        reader = PdfReader(f"data/{filename}")
        text = "\n".join([page.extract_text() for page in reader.pages if page.extract_text()])
        if not text:
            print(f"[Warning] No text found in: {filename}")
        all_texts.append((filename, text))

# Step 2: Chunk and tag
splitter = RecursiveCharacterTextSplitter(chunk_size=800, chunk_overlap=200)
chunks = []
for source_name, text in all_texts:
    for chunk in splitter.split_text(text):
        chunks.append({"text": chunk, "source": source_name})

# Step 3: Embed
model = SentenceTransformer("all-MiniLM-L6-v2")
texts = [c["text"] for c in chunks]
embeddings = model.encode(texts)

# Step 4: Save chunks + embeddings
with open("chunks.pkl", "wb") as f:
    pickle.dump((chunks, embeddings), f)

print(f"✅ Processed and saved {len(chunks)} chunks from {len(all_texts)} PDFs.")
