import pdfplumber
import streamlit as st
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_openai import OpenAIEmbeddings, OpenAI
from langchain_community.vectorstores import FAISS
from langchain_core.output_parsers import StrOutputParser
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.runnables import RunnablePassthrough
import os

OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")

st.header("My First Chatbot")

with st.sidebar:
    st.title("Your Documents")
    file = st.file_uploader("Upload a PDF file and start asking questions", type="pdf")

#Extract contents from the PDF and chunk it
if file is not None:
    #extract the text from it
    with pdfplumber.open(file) as pdf:
        text = ""
        for page in pdf.pages:
            text += page.extract_text() + "\n"
    #st.write(text)

    #Split text into chunks
    text_splitter = RecursiveCharacterTextSplitter(
        separators = ["\n\n", "\n", ". ", " ", ""],
        chunk_size = 1000,
        chunk_overlap = 200
    )
    chunks = text_splitter.split_text(text)
    #st.write(chunks)

    #Generating embeddings
    embeddings = OpenAIEmbeddings(
        model = "text-embedding-3-small",
        api_key = OPENAI_API_KEY
    )
    
    #Store embeddings in vector db
    vector_store = FAISS.from_texts(chunks, embeddings)

    #Get user question
    user_question = st.text_input("Type your question here")

    #generate answer
    #question -> embeddings -> similiarity search -> results to LLM -> response (CHAIN)

    def format_docs(dosc):
        return "\n\n".join([doc.page_content for doc in docs])

    retriever = vector_store.as_retriever(
        search_type = "mmr",
        search_kwargs = {"k":4} #4 closest matches
    )

    #what color is apple - 397654567
    #red, green, yellow -- 89956232, 156456112, 123454665

    llm = OpenAI(
        model = "gpt-4o-mini",
        temperature = 0.3,
        max_tokens = 1000,
        api_key = OPENAI_API_KEY
    )

    prompt = ChatPromptTemplate.from_messages([
        ("system",
         "You are a helpful assistan answering questions about a PDF document.\n\n"
         "Guidelines:\n"
         "1. Provide a complete, well-explained answers using the context below.\n"
         "2. Include relevant details, numbers, and explanations to give a through response.\n"
         "3. If the context mentions related information, include it to give fuller picture.\n"
         "4. Only use information from the provided context - do not use outside knowledge.\n"
         "5. Summarize long information, ideally in bullets where needed\n"
         "6. If the information is not in the context, say so plitely.\n\n"
         "Context:\n{context}"),
         ("human", "{question}")     
    ])

    chain = (
        {"context": retriever | format_docs, "question": RunnablePassthrough()}
        | prompt
        | llm
        | StrOutputParser()
    )

    if user_question:
        response = chain.invoke(user_question)
        st.write(response)