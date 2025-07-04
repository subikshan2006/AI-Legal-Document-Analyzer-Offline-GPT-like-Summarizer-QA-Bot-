# AI Legal Document Analyzer - Offline Document QA using FAISS + Embeddings

import os
import fitz  # PyMuPDF
import faiss
import numpy as np
from sentence_transformers import SentenceTransformer
from langchain.text_splitter import RecursiveCharacterTextSplitter

# Load model
model = SentenceTransformer('all-MiniLM-L6-v2')

# Load and read PDF
def extract_text_from_pdf(file_path):
    doc = fitz.open(file_path)
    text = ""
    for page in doc:
        text += page.get_text()
    return text

# Split into chunks
def split_text(text, chunk_size=500, overlap=50):
    splitter = RecursiveCharacterTextSplitter(chunk_size=chunk_size, chunk_overlap=overlap)
    return splitter.split_text(text)

# Embed text and store in FAISS
def create_vector_store(chunks):
    vectors = model.encode(chunks)
    index = faiss.IndexFlatL2(len(vectors[0]))
    index.add(np.array(vectors))
    return index, vectors

# Search for relevant chunks
def search_query(index, chunks, query, top_k=3):
    query_vector = model.encode([query])
    D, I = index.search(query_vector, top_k)
    results = [chunks[i] for i in I[0]]
    return results

def main():
    print("📄 Loading legal document...")
    file_path = "data/contract.pdf"
    raw_text = extract_text_from_pdf(file_path)

    print("✂️ Splitting into chunks...")
    chunks = split_text(raw_text)

    print("🔍 Creating vector store...")
    index, _ = create_vector_store(chunks)

    print("🤖 Ask a question about the document:")
    query = input("🔎 Your Question: ")
    results = search_query(index, chunks, query)

    print("\n📚 Top Answers:")
    for i, r in enumerate(results, 1):
        print(f"Answer {i}: {r.strip()}\n")

if __name__ == "__main__":
    main()
