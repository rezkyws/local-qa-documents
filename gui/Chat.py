import streamlit as st
import requests

st.title("💬 Chat with your docs on database")
st.sidebar.success("Select Any Page from here")

if "messages" not in st.session_state:
    st.session_state["messages"] = [
        {"role": "assistant", "content": "Hi, I'm a chatbot who will ask question based on your docs on your database. How can I help you?"}
    ]

for msg in st.session_state.messages:
    st.chat_message(msg["role"]).write(msg["content"])

if prompt := st.chat_input(placeholder="What is algorithm ?"):
    st.session_state.messages.append({"role": "user", "content": prompt})
    st.chat_message("user").write(prompt)

    with st.chat_message("assistant"):
        # st_cb = StreamlitCallbackHandler(st.container(), expand_new_thoughts=False)
        response = requests.post('http://localhost:3347/api/v1/chat', json={"question": prompt}, timeout=60).json()
        # response = search_agent.run(st.session_state.messages, callbacks=[st_cb])
        raw_source_documents = response["result"]["source_docs"]
        source_documents = '**Source documents (index)** : '
        for docs in raw_source_documents:
            index = docs['metadata']['start_index']
            source_documents += f'{index}, '
        answer = response["result"]["answer"]
        st.session_state.messages.append({"role": "assistant", "content": answer+ "\n\n\n" + source_documents})
        st.write(answer)
        st.write("\n")
        st.write(source_documents)