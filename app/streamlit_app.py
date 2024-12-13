import streamlit as st
from openai import OpenAI

client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))
import os

# Set OpenAI API key

# Ensure the API key is set
if not openai.api_key:
    st.error("OpenAI API key not found. Please set the 'OPENAI_API_KEY' environment variable.")
    st.stop()

import time

# Set up the header
st.header("Measuring System-Wide Contribution Towards the SDGs")

# Initialize session state
if "messages" not in st.session_state:
    st.session_state.messages = [
        {"role": "assistant", "content": "Ask me a question about System-Wide reporting"}
    ]

# Display chat messages from history on app rerun
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# React to user input
if prompt := st.chat_input("What is up?"):
    # Display user message in chat message container
    st.chat_message("user").markdown(prompt)

    # Add user message to history
    st.session_state.messages.append({"role": "user", "content": prompt})

    try:
        # Call the OpenAI API to get a response
        response = client.chat.completions.create(model="gpt-4",  # Ensure to use a suitable model, e.g., GPT-4 or GPT-3.5
        messages=st.session_state.messages)

        # Extract assistant's response
        assistant_response = response.choices[0].message.content

        # Display assistant response in chat message container
        with st.chat_message("assistant"):
            st.markdown(assistant_response)

        # Add assistant response to chat history
        st.session_state.messages.append({"role": "assistant", "content": assistant_response})
    except Exception as e:
        st.error(f"An error occurred: {e}")
