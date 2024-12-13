import streamlit as st
import openai
import os

# Streamlit app header
st.header("Measuring System-Wide Contribution Towards the SDGs")

# Load OpenAI API key from environment variables
openai.api_key = os.getenv("OPENAI_API_KEY")

# Define initial system message for the assistant
SYSTEM_MESSAGE = {"role": "system", "content": "You are a helpful assistant."}
INITIAL_PROMPT = {"role": "assistant", "content": "Ask me a question about System-Wide reporting"}

# Initialize session state variables
if "messages" not in st.session_state:
    st.session_state.messages = [SYSTEM_MESSAGE, INITIAL_PROMPT]

# Display chat history on app rerun
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# React to user input
if prompt := st.chat_input("What is up?"):
    # Display user message in chat container
    st.chat_message("user").markdown(prompt)

    # Add user message to session state
    st.session_state.messages.append({"role": "user", "content": prompt})

    # Generate response from OpenAI
    try:
        response = openai.ChatCompletion.create(
            model="gpt-4",
            messages=st.session_state.messages,
            max_tokens=150
        )

        # Extract assistant response
        assistant_response = response["choices"][0]["message"]["content"]

        # Display assistant response in chat container
        with st.chat_message("assistant"):
            st.markdown(assistant_response)

        # Add assistant response to session state
        st.session_state.messages.append({"role": "assistant", "content": assistant_response})

    except openai.error.OpenAIError as e:
        # Handle API errors gracefully
        with st.chat_message("assistant"):
            st.markdown(f"**Error:** {e}")
