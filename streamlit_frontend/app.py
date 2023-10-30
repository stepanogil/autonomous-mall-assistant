import streamlit as st
import random
from backend import chat
from streamlit_chat import message

# Streamlit app
st.header("Mall Assistant Chatbot")
st.markdown("Ask questions about store locations, promotions, and more.")

if "past" not in st.session_state:
    st.session_state["past"] = []
if "generated" not in st.session_state:
    st.session_state["generated"] = []

if "input_message_key" not in st.session_state:
    st.session_state["input_message_key"] = str(random.random())

chat_container = st.container()

user_input = st.text_input("Type your message and press Enter to send.", key=st.session_state["input_message_key"])

if st.button("Send"):
    response = chat(user_input)

    st.session_state["past"].append(user_input)
    st.session_state["generated"].append(response)

    st.session_state["input_message_key"] = str(random.random())

    st.experimental_rerun()

if st.session_state["generated"]:
    with chat_container:
        for i in range(len(st.session_state["generated"])):
            message(st.session_state["past"][i], is_user=True, key=str(i) + "_user")
            message(st.session_state["generated"][i], key=str(i))

