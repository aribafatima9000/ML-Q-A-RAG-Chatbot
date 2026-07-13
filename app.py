
import streamlit as st
from rag import create_database, ask_question

st.set_page_config(page_title="Simple RAG")

st.title("📄 Simple RAG Chatbot")

if st.button("Create Database"):

    with st.spinner("Creating Database..."):
        create_database()

    st.success("Database Created Successfully!")

question = st.text_input("Ask Your Question")

if st.button("Get Answer"):

    if question == "":
        st.warning("Enter a question")

    else:

        with st.spinner("Thinking..."):

            answer = ask_question(question)

        st.write(answer)