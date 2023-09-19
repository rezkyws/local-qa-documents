import streamlit as st
import requests

# with st.sidebar:
#     openai_api_key = st.text_input("OpenAI API Key", key="langchain_search_api_key_openai", type="password")
#     "[Get an OpenAI API key](https://platform.openai.com/account/api-keys)"
#     "[View the source code](https://github.com/streamlit/llm-examples/blob/main/pages/2_Chat_with_search.py)"
#     "[![Open in GitHub Codespaces](https://github.com/codespaces/badge.svg)](https://codespaces.new/streamlit/llm-examples?quickstart=1)"

# st.set_page_config(page_title = "This is a Multipage WebApp")
st.title("💬 Chat with your docs on database")
st.sidebar.success("Select Any Page from here")

# """
# In this example, we're using `StreamlitCallbackHandler` to display the thoughts and actions of an agent in an interactive Streamlit app.
# Try more LangChain 🤝 Streamlit Agent examples at [github.com/langchain-ai/streamlit-agent](https://github.com/langchain-ai/streamlit-agent).
# """

if "messages" not in st.session_state:
    st.session_state["messages"] = [
        {"role": "assistant", "content": "Hi, I'm a chatbot who will ask question based on your docs on your database. How can I help you?"}
    ]

for msg in st.session_state.messages:
    st.chat_message(msg["role"]).write(msg["content"])

if prompt := st.chat_input(placeholder="What is algorithm ?"):
    st.session_state.messages.append({"role": "user", "content": prompt})
    st.chat_message("user").write(prompt)

    # if not openai_api_key:
    #     st.info("Please add your OpenAI API key to continue.")
    #     st.stop()

    # llm = ChatOpenAI(model_name="gpt-3.5-turbo", openai_api_key=openai_api_key, streaming=True)
    # search = DuckDuckGoSearchRun(name="Search")
    # search_agent = initialize_agent([search], llm, agent=AgentType.ZERO_SHOT_REACT_DESCRIPTION, handle_parsing_errors=True)
    with st.chat_message("assistant"):
        # st_cb = StreamlitCallbackHandler(st.container(), expand_new_thoughts=False)
        response = requests.post('http://localhost:3345/api/v1/chat', json={"question": prompt}, timeout=60).json()
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