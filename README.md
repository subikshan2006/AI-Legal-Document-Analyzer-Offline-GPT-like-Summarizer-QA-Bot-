# 🧠 AI Legal Document Analyzer (Offline GPT-like QA System for Contracts)

This project builds an offline AI tool that lets you ask questions about legal documents — just like a private ChatGPT, but focused on legal contracts and agreements.

> No cloud. No API. Just pure local intelligence with embeddings, FAISS, and Python.

---

## 📌 Overview

- 📄 Upload a legal document (PDF format)
- ✂️ Automatically splits the text into chunks
- ⚙️ Uses `sentence-transformers` to generate embeddings
- 🔍 Stores embeddings in a local FAISS index
- ❓ You ask questions — it returns the best-matching clauses

---

## 🎯 Why This Project?

✅ Shows real-world understanding of NLP  
✅ Demonstrates offline vector search with legal language  
✅ Perfect for contract analysis, legal tech demos, or job applications  
✅ Looks like enterprise-grade work for recruiters or AI/ML hiring managers

---

## 🧠 Tech Stack

| Task                      | Library                        |
|---------------------------|---------------------------------|
| PDF Parsing               | `PyMuPDF` (fitz)                |
| Text Splitting            | `langchain.text_splitter`       |
| Sentence Embeddings       | `sentence-transformers`         |
| Similarity Search         | `faiss-cpu`                     |
| Language                  | Python                          |

> Model used: `all-MiniLM-L6-v2` — small, fast, and accurate for semantic search.

---

## 📁 Project Structure
```
legal_doc_analyzer/
├── main.py
├── README.md
├── data/
│ └── contract.pdf

yaml
Copy
Edit
```
---

## 🔧 Setup Instructions
```
 1. Install required libraries:

bash
pip install sentence-transformers faiss-cpu pymupdf langchain
2. Prepare your legal document
Put your contract or agreement in data/contract.pdf

You can use any realistic document — employment, service agreement, etc.

3. Run the tool:
bash
Copy
Edit
python main.py
Then type your questions like:

csharp
Copy
Edit
🔎 Your Question: What is the duration of the agreement?
✅ Sample Output
sql
Copy
Edit
📚 Top Answers:
Answer 1: This Agreement shall commence on January 1, 2025, and shall remain in effect for a period of 12 months unless terminated earlier...

Answer 2: The Agreement is effective for 1 year from the date of execution.
💼 Real Use Cases
AI resume screeners for legal hiring teams

Offline contract reviewers for privacy-critical environments

College students demonstrating offline GPT-style tools

Legal tech startups prototyping intelligent search

🚀 Future Enhancements
PDF-to-text highlighting for answer locations

Streamlit web interface for non-programmers

Integration with LLaMA 3 for natural-sounding answers

Summarization + QA combo module


```
### 🧑‍💻 Author
Subikshan P

B.Tech Artificial Intelligence & Machine Learning (AIML)

Saveetha Engineering College, Chennai

Graduating: 2027

GitHub: [github.com/subikshan2006](https://github.com/subikshan2006)

LinkedIn:(https://www.linkedin.com/in/subikshan-p-7a7002317/)

