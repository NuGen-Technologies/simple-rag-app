# simple-rag-app

🧠 How RAG Works
Retrieval-Augmented Generation (RAG) is a technique that combines document retrieval with language generation to create highly contextual answers from your own data.

🔄 RAG Workflow in This App
📥 Input Query
A user types a question in the web interface.

📚 Document Retrieval
Relevant chunks are retrieved from PDFs, text files, and web pages using FAISS and semantic similarity.

🧠 Contextual Answer Generation
The Groq LLM (llama3-8b-8192) uses the input + retrieved documents to generate accurate, context-aware answers.

🧩 Inside the Code
code includes the following components:

## Project Banner

![Project Banner](assets/banner.png)


File/Directory	Description

app.py:	Streamlit/Flask web app for UI and question answering

utils.py: (optional)	Helper functions for loading docs, vector creation, and embeddings

data/	Stores:  sample PDFs and text files (e.g., DeepLearning.pdf)

faiss_index/	: Folder where vector embeddings are stored locally

.env :	Stores GROQ_API_KEY securely

requirements.txt :	List of all required dependencies

💻 How to Use This RAG Application
✅ Prerequisites
Python 3.8 or above

pip (Python package installer)
A valid GROQ_API_KEY (Free from Groq)



