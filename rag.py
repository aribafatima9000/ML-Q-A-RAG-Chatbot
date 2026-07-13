from langchain_community.document_loaders import PyPDFLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_community.embeddings import HuggingFaceEmbeddings
from langchain_community.vectorstores import FAISS
from langchain_groq import ChatGroq
import os


def create_database():

    pdf_path = "1773455552333.pdf"

    if not os.path.exists(pdf_path):
        raise FileNotFoundError(f"{pdf_path} not found.")

    loader = PyPDFLoader(pdf_path)
    documents = loader.load()

    splitter = RecursiveCharacterTextSplitter(
        chunk_size=500,
        chunk_overlap=50
    )

    chunks = splitter.split_documents(documents)

    embedding = HuggingFaceEmbeddings(
        model_name="sentence-transformers/all-MiniLM-L6-v2"
    )

    db = FAISS.from_documents(chunks, embedding)

    db.save_local("faiss_db")


def ask_question(question):

    embedding = HuggingFaceEmbeddings(
        model_name="sentence-transformers/all-MiniLM-L6-v2"
    )

    db = FAISS.load_local(
        "faiss_db",
        embedding,
        allow_dangerous_deserialization=True
    )

    docs = db.similarity_search(question)

    context = ""

    for doc in docs:
        context += doc.page_content + "\n"

    

    llm = ChatGroq(
    groq_api_key="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",
    model_name="llama-3.3-70b-versatile"
)

    prompt = f"""
Answer only from the given context.

Context:
{context}

Question:
{question}
"""

    response = llm.invoke(prompt)

    return response.content