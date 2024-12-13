import streamlit as st
import openai
import time
import os

st.header("Measuring System-Wide Contribution Towards the SDGs")

openai.api_key = os.getenv("OPENAI_API_KEY")

assistant_id = "asst_EqzTmhPzlSEXg6BP66qsN16J"

if "thread" not in st.session_state.keys():
    thread = openai.beta.threads.create()
    st.session_state.thread= thread.id

if "messages" not in st.session_state.keys():
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

    #Create a message
    st.session_state.messages.append({"role": "user", "content": prompt})
    message = openai.beta.threads.messages.create(
        thread_id=st.session_state.thread,
        role="user",
        content=prompt,
    )

    #Create a run

    run = openai.beta.threads.runs.create(
        thread_id=st.session_state.thread,
        assistant_id=assistant_id,
    )

    while True:
        time.sleep(1)
        if openai.beta.threads.runs.retrieve(thread_id=st.session_state.thread, run_id=run.id).status in ['completed', 'failed', 'requires_action']:
            break
    if openai.beta.threads.runs.retrieve(thread_id=st.session_state.thread, run_id=run.id).status == 'failed':
        print(run.error)

    messages = openai.beta.threads.messages.list(
    thread_id=st.session_state.thread
    )
    response = messages.data[0].content[0].text.value
    
    # Display assistant response in chat message container
    with st.chat_message("assistant"):
        st.markdown(response)
    # Add assistant response to chat history
    st.session_state.messages.append({"role": "assistant", "content": response})