import streamlit as st
import ollama
import time

# Streamlit UI Configuration
st.set_page_config(page_title="Ollama AI Chatbot", page_icon="🤖", layout="wide")

st.title("🤖 Shivtej Mishra Personal AI Bot")
st.markdown("Chat with a locally running AI model powered by **Ollama**.")

# Fetch installed models dynamically and handle different structures
try:
    models_data = ollama.list()
    models_list = [model.get("name", model.get("model", "Unknown Model")) for model in models_data.get("models", [])]

    if not models_list:
        st.warning("⚠️ No models found in Ollama. Please install a model using `ollama pull <model_name>`.")
        models_list = ["No models available"]

except Exception as e:
    st.error(f"Error fetching models: {e}")
    models_list = ["Error fetching models"]

# Sidebar for model selection
with st.sidebar:
    st.header("⚙️ Settings")
    selected_model = st.selectbox("Choose AI Model", models_list, index=0)

if selected_model in ["No models available", "Error fetching models"]:
    st.stop()  # Stop execution if no valid models exist

st.write(f"**🧠 Current Model:** `{selected_model}`")

# Chat history storage
if "messages" not in st.session_state:
    st.session_state.messages = []

# Display previous chat history
for msg in st.session_state.messages:
    with st.chat_message(msg["role"]):
        st.markdown(msg["content"])

# User input
prompt = st.chat_input("Type your message...")

if prompt:
    # Display user message instantly
    st.chat_message("user").markdown(prompt)

    # Placeholder for AI response (for streaming effect)
    with st.chat_message("assistant"):
        message_placeholder = st.empty()

        # Call Ollama with the selected model
        try:
            response = ollama.chat(model=selected_model, messages=[{"role": "user", "content": prompt}], stream=True)

            bot_reply = ""  # Store full response

            # Stream response word by word
            for chunk in response:
                if "message" in chunk and "content" in chunk["message"]:
                    new_text = chunk["message"]["content"]
                    bot_reply += new_text  # Append to full response

                    # Update UI with a typewriter effect
                    message_placeholder.markdown(bot_reply + "▌")  # Cursor effect
                    time.sleep(0.05)  # Adjust speed for smooth animation

            # Final update (remove cursor effect)
            message_placeholder.markdown(bot_reply)

            # Save conversation to history
            st.session_state.messages.append({"role": "user", "content": prompt})
            st.session_state.messages.append({"role": "assistant", "content": bot_reply})

        except Exception as e:
            st.error(f"Error communicating with the model: {e}")
