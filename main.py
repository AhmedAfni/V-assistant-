from langchain_google_genai import GoogleGenerativeAI
import streamlit as st
import random
import time


llm = GoogleGenerativeAI(model="gemini-pro", google_api_key= "AIzaSyARruYpjQSzQh0P8-Qy3-qIcbmz1B1FJSY")


st.title("V-ASSISTANT")

# Initialize chat history
if "messages" not in st.session_state:
    st.session_state.messages = []

# Display chat messages from history on app rerun
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# Accept user input
if prompt := st.chat_input("What is up?"):
    # Add user message to chat history
    st.session_state.messages.append({"role": "user", "content": prompt})
    # Display user message in chat message container
    with st.chat_message("user"):
        st.markdown(prompt)

    # Display assistant response in chat message container
    with st.chat_message("assistant"):
        response = llm.invoke(prompt)
        st.write(response)
    # Add assistant response to chat history
    st.session_state.messages.append({"role": "assistant", "content": response})