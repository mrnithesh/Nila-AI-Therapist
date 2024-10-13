import os
import google.generativeai as genai
import strip_markdown
import pyttsx3
import threading

def generate_and_play_audio(text):
    """Generate and play TTS audio from text using pyttsx3."""
    engine = pyttsx3.init()
    engine = pyttsx3.init()
    voices = engine.getProperty('voices')
    engine.setProperty('voice', voices[1].id)  # Try different indices to change voices
    engine.setProperty('rate', 150)  # Speed of speech
    engine.setProperty('volume', 0.9)  # Volume (0.0 to 1.0)
    engine.say(text)
    engine.runAndWait()

def convo(query):
    response = chat.send_message(query)
    updated_response = strip_markdown.strip_markdown(response.text)
    print(updated_response)
    
    # Start audio generation and playback in a separate thread
    audio_thread = threading.Thread(target=generate_and_play_audio, args=(updated_response,))
    audio_thread.start()

# Retrieve Google API Key
GOOGLE_API_KEY = os.getenv("GEMINI_API_KEY")   # Set your API key here
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
    model_name="gemini-1.5-flash",
    generation_config=generation_config,
    safety_settings=safety_settings
)

chat = model.start_chat(history=[])

# Initialize conversation with system instruction
convo(system_instruction)

# Main interaction loop
while True:
    query = input("What's on your mind? :")
    if query.lower() in {"exit", "quit", "bye"}:
        print("Goodbye! Have a great day!")
        break
    convo(query)
