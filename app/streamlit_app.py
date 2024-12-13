import streamlit as st
from openai import OpenAI

client = OpenAI(api_key="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")
import time

# Set up the header
st.header("Measuring System-Wide Contribution Towards the SDGs")

# Set your OpenAI API key

# Check if the session state has the 'thread' key
if "thread" not in st.session_state:
    # Create a new thread using OpenAI API (for chat purposes)
    response = client.chat.completions.create(model="gpt-4",  # Ensure to use a suitable model, e.g., GPT-4 or GPT-3.5
    messages=[{"role": "system", "content": "You are a helpful assistant."}])
    st.session_state.thread = response.id

# Initialize message history if it doesn't exist
if "messages" not in st.session_state:
    st.session_state.messages = [
        {"role": "assistant", "content": "Ask me a question about Systems-Wide reporting"}
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

    # Call the OpenAI API to send the message and get a response
    response = client.chat.completions.create(model="gpt-4",  # Ensure to use a suitable model, e.g., GPT-4 or GPT-3.5
    messages=st.session_state.messages)

    assistant_response = response.choices[0].message.content

    # Display assistant response in chat message container
    with st.chat_message("assistant"):
        st.markdown(assistant_response)

    # Add assistant response to chat history
    st.session_state.messages.append({"role": "assistant", "content": assistant_response})
