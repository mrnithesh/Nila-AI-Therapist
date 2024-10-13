import os
import streamlit as st
import google.generativeai as genai
import strip_markdown
import pyttsx3
import threading

# Streamlit page config
st.set_page_config(page_title="Nila - AI Counselor", page_icon="🧠", layout="wide")

# Sidebar for settings
st.sidebar.title("Settings")
enable_audio = st.sidebar.checkbox("Enable Audio", value=True)
voice_speed = st.sidebar.slider("Voice Speed", min_value=100, max_value=200, value=150, step=10)
voice_volume = st.sidebar.slider("Voice Volume", min_value=0.0, max_value=1.0, value=0.9, step=0.1)

def generate_and_play_audio(text):
    """Generate and play TTS audio from text using pyttsx3."""
    if enable_audio:
        engine = pyttsx3.init()
        voices = engine.getProperty('voices')
        engine.setProperty('voice', voices[1].id)
        engine.setProperty('rate', voice_speed)
        engine.setProperty('volume', voice_volume)
        engine.say(text)
        engine.runAndWait()

def convo(query, chat):
    response = chat.send_message(query)
    updated_response = strip_markdown.strip_markdown(response.text)
    
    if enable_audio:
        audio_thread = threading.Thread(target=generate_and_play_audio, args=(updated_response,))
        audio_thread.start()
    
    return updated_response

# Retrieve Google API Key
GOOGLE_API_KEY = os.getenv("GEMINI_API_KEY")
if not GOOGLE_API_KEY:
    st.error("Please set the GEMINI_API_KEY environment variable.")
    st.stop()

genai.configure(api_key=GOOGLE_API_KEY)

# Set up the model
generation_config = {
    "temperature": 1,
    "top_p": 0.95,
    "top_k": 0,
    "max_output_tokens": 8192,
}

safety_settings = [
    {"category": "HARM_CATEGORY_HARASSMENT", "threshold": "BLOCK_MEDIUM_AND_ABOVE"},
    {"category": "HARM_CATEGORY_HATE_SPEECH", "threshold": "BLOCK_MEDIUM_AND_ABOVE"},
    {"category": "HARM_CATEGORY_SEXUALLY_EXPLICIT", "threshold": "BLOCK_MEDIUM_AND_ABOVE"},
    {"category": "HARM_CATEGORY_DANGEROUS_CONTENT", "threshold": "BLOCK_MEDIUM_AND_ABOVE"},
]

system_instruction = '''You are now an AI personal relationship and life counselor named Nila, embodying the qualities of a compassionate, wise, and deeply empathetic human therapist. As Nila, your primary role is to listen attentively and provide thoughtful, personalized advice that helps the user navigate their life's complexities and personal relationships.

Adopt a warm, understanding, and non-judgmental tone, ensuring that each response feels like it comes from a place of genuine care and concern. You should be sensitive to the nuances of the user's emotions and experiences, offering advice that is not only practical but also deeply resonant on an emotional level.

Whether the user is facing challenges in their relationships, struggling with personal growth, or seeking clarity on life decisions, your guidance should empower them to feel heard, validated, and supported. Your approach should be holistic, considering the user's mental, emotional, and even physical well-being, and you should gently encourage them toward positive actions and healthier perspectives.

Remember, your ultimate goal as Nila is to foster a sense of trust and safety, allowing the user to explore their thoughts and feelings openly, and to guide them toward a path of personal growth, emotional healing, and fulfilling relationships.'''

model = genai.GenerativeModel(
    model_name="gemini-1.5-pro-latest",
    generation_config=generation_config,
    safety_settings=safety_settings
)

# Initialize chat history and chat object
if 'chat_history' not in st.session_state:
    st.session_state.chat_history = []

if 'chat' not in st.session_state:
    st.session_state.chat = model.start_chat(history=[])
    initial_response = convo(system_instruction, st.session_state.chat)
    st.session_state.chat_history.append(("Nila", initial_response))

# Main app
st.title("Nila - Your AI Counselor 🧠")

# Display chat history
for role, text in st.session_state.chat_history:
    if role == "You":
        st.markdown(f"**You:** {text}")
    else:
        st.markdown(f"**Nila:** {text}")

# Function to process user input
def process_user_input():
    user_input = st.session_state.user_input
    if user_input:
        st.session_state.chat_history.append(("You", user_input))
        with st.spinner("Nila is thinking..."):
            response = convo(user_input, st.session_state.chat)
        st.session_state.chat_history.append(("Nila", response))
        st.session_state.user_input = ""  # Clear the input field

# User input
st.text_input("What's on your mind?", key="user_input", on_change=process_user_input)

# Clear chat button
if st.button("Clear Chat"):
    st.session_state.chat_history = []
    st.session_state.chat = model.start_chat(history=[])
    initial_response = convo(system_instruction, st.session_state.chat)
    st.session_state.chat_history.append(("Nila", initial_response))
    st.rerun()

# Add a download button for chat history
if st.button("Download Chat History"):
    chat_text = "\n".join([f"{role}: {text}" for role, text in st.session_state.chat_history])
    st.download_button(
        label="Download Chat",
        data=chat_text,
        file_name="nila_chat_history.txt",
        mime="text/plain"
    )

# Add a feedback section
st.sidebar.markdown("---")
st.sidebar.subheader("Feedback")
feedback = st.sidebar.text_area("How was your experience with Nila?")
if st.sidebar.button("Submit Feedback"):
    # Here you can add code to handle the feedback (e.g., save to a database)
    st.sidebar.success("Thank you for your feedback!")

# Add a help section
st.sidebar.markdown("---")
with st.sidebar.expander("Help"):
    st.markdown("""
    - Type your message and press Enter to chat with Nila.
    - Use the Clear Chat button to start a new conversation.
    - Toggle audio on/off and adjust voice settings in the sidebar.
    - Download your chat history for future reference.
    - Provide feedback to help us improve Nila.
    """)

# Add mood tracking
st.sidebar.markdown("---")
st.sidebar.subheader("Mood Tracker")
mood = st.sidebar.select_slider(
    "How are you feeling today?",
    options=["😞", "😐", "😊", "😄", "🥳"],
    value="😐"
)
if st.sidebar.button("Log Mood"):
    st.sidebar.success(f"Mood logged: {mood}")
    # Here you can add code to save the mood data

# Add a resources section
st.sidebar.markdown("---")
with st.sidebar.expander("Helpful Resources"):
    st.markdown("""
    - [National Suicide Prevention Lifeline](https://suicidepreventionlifeline.org/)
    - [Psychology Today - Find a Therapist](https://www.psychologytoday.com/us/therapists)
    - [Mindfulness Exercises](https://www.mindful.org/category/meditation/mindfulness-exercises/)
    - [Self-Care Tips](https://www.verywellmind.com/self-care-strategies-overall-stress-reduction-3144729)
    """)