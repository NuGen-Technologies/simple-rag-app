from flask import Flask, render_template, request, jsonify
from langchain_community.vectorstores import FAISS
from langchain_huggingface import HuggingFaceEmbeddings
from langchain.chains import RetrievalQA
from langchain_groq import ChatGroq
from dotenv import load_dotenv
import os

load_dotenv()
app = Flask(__name__)

# Load embedding model
embedding_model = HuggingFaceEmbeddings(model_name="all-MiniLM-L6-v2")

# Load FAISS vector store
vector_store = FAISS.load_local("faiss_index", embedding_model, allow_dangerous_deserialization=True)
retriever = vector_store.as_retriever()

# Load LLM from Groq
llm = ChatGroq(
    temperature=0,
    model_name="llama3-8b-8192",  # or "mixtral-8x7b-32768" if needed
    groq_api_key=os.getenv("GROQ_API_KEY")
)

# Build RAG chain
qa_chain = RetrievalQA.from_chain_type(llm=llm, retriever=retriever)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/ask", methods=["POST"])
def ask():
    question = request.json.get("question")
    if not question:
        return jsonify({"error": "No question provided"}), 400
    answer = qa_chain.run(question)
    return jsonify({"answer": answer})

if __name__ == "__main__":
    app.run(debug=True)
