import streamlit as st
import openai
import time

# Set up the header
st.header("Measuring System-Wide Contribution Towards the SDGs")

# Set your OpenAI API key
openai.api_key = "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"

# Check if the session state has the 'thread' key
if "thread" not in st.session_state:
    # Create a new thread using OpenAI API (for chat purposes)
    response = openai.ChatCompletion.create(
        model="gpt-4",  # Ensure to use a suitable model, e.g., GPT-4 or GPT-3.5
        messages=[{"role": "system", "content": "You are a helpful assistant."}]
    )
    st.session_state.thread = response['id']

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
    response = openai.ChatCompletion.create(
        model="gpt-4",  # Ensure to use a suitable model, e.g., GPT-4 or GPT-3.5
        messages=st.session_state.messages
    )

    assistant_response = response['choices'][0]['message']['content']
    
    # Display assistant response in chat message container
    with st.chat_message("assistant"):
        st.markdown(assistant_response)

    # Add assistant response to chat history
    st.session_state.messages.append({"role": "assistant", "content": assistant_response})