# Nila-AI Therapist

**Nila-AI** is an advanced conversational AI chatbot designed to provide compassionate and insightful guidance on personal relationships and life challenges. Built using Google’s Generative AI API for natural language understanding and **pyttsx3** for faster, offline Text-to-Speech (TTS) responses, it serves as a virtual therapist for users seeking emotional support.

## Key Features

- **Natural Language Understanding**: Nila-AI leverages Google Generative AI to respond intelligently and contextually.
- **Offline Text-to-Speech**: Integrated with `pyttsx3` for real-time, offline voice responses with minimal delay.
- **Scalable Architecture**: Designed for smooth deployment and interaction.

## Getting Started

### 1. Clone the Repository
```bash
git clone https://github.com/mrnithesh/Nila-AI-Therapist.git
cd Nila-AI-Therapist
```

### 2. Install Dependencies
Ensure you have Python 3.x installed. Then, install the required Python libraries:
```bash
pip install -r requirements.txt
```

### 3. Set Up API Keys
To use Google Generative AI, configure your API key:
```python
genai.configure(api_key="YOUR_GOOGLE_API_KEY")
```

### 4. Run the Application
```bash
python main.py
```

## Documentation & References

- [Google Generative AI Documentation](https://cloud.google.com/generative-ai)
- [pyttsx3 Text-to-Speech Documentation](https://pypi.org/project/pyttsx3/)
- [Python Google API Client](https://googleapis.dev/python/google-api-core/latest/index.html)

For more detailed API integration or advanced use cases, please refer to the above official documentation.

## Project Structure

- **main.py**: Contains the core logic with updated Text-to-Speech functionality using `pyttsx3`.
- **requirements.txt**: Lists the required dependencies.
- **legacy/**: Contains the original Jupyter Notebook (`Nila_AI_Therapist.ipynb`) for historical reference.

## How It Works

The chatbot interacts via the terminal, responding to user inputs with text and audio. It uses Google Generative AI for generating meaningful replies, while `pyttsx3` provides offline, faster TTS with minimal delay compared to online TTS services.

### Core Workflow:
1. **Input**: User queries.
2. **Processing**: Google Generative AI analyzes the query and generates a response.
3. **Output**: The response is either returned as text or spoken aloud using `pyttsx3`.

## Contributing

Feel free to contribute by forking the repository, making your changes, and submitting a pull request. Suggestions to improve functionality or add new features are always welcome.

## License

This project is licensed under the [MIT License](LICENSE).

## Contact

For any queries or further information, please reach out via [LinkedIn](https://www.linkedin.com/in/mrnithesh/) or email at mr.nithesh.k@gmail.com.


