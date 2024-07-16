
# Nila-AI-Therapist


## Overview

The Nila-AI Therapy Chatbot is a conversational AI designed to provide advice and guidance on personal relationships and life issues. It utilizes Google's Generative AI API for natural language generation and Google Text-to-Speech (gTTS) for audio feedback.

## Features

- **Interactive Conversations**: Engage in conversations with the chatbot about personal relationships and life issues.
- **Text-to-Speech Conversion**: Convert chatbot responses into spoken audio for a more interactive experience.
- **Integration with Google Colab**: Designed to work seamlessly in Google Colab notebooks.

## Usage

### Getting Started

To use the AI Therapy Chatbot, follow these steps:

1. **Set Up Google Colab**:
   - Open the provided Colab notebook (`Nila-AI Therapist.ipynb`) in Google Colab.

2. **Install Dependencies**:
   - Ensure you have the necessary dependencies installed:
     ```python
     !pip install google-generativeai gtts
     ```

3. **Set Up Google API Key**:
   - Obtain a Google API key for the Generative AI API and set it in your Colab notebook.

4. **Run the Notebook**:
   - Execute the cells in the notebook to initialize the chatbot and start interacting with it.

### Example Usage

```python
# Example usage in Google Colab
import google.generativeai as genai
from gtts import gTTS
import io

# Configure Google API key
genai.configure(api_key="YOUR_GOOGLE_API_KEY")

# Initialize chatbot model and start interaction
# Insert code snippet from your notebook
```

### API Reference

- **google.generativeai**: Documentation for using Google's Generative AI API can be found [here](https://google.github.io/generativeai-python/).

- **gtts**: Documentation for gTTS (Google Text-to-Speech) can be found [here](https://gtts.readthedocs.io/en/latest/).

### Contributing

We welcome contributions to improve the AI Therapy Chatbot! If you'd like to contribute, please follow these guidelines:

- Fork the repository and create your branch from `main`.
- Follow the coding style and guidelines used in the project.
- Make sure to test your changes thoroughly.
- Submit a pull request detailing the changes made and the problem solved.

### License

This project is licensed under the [MIT License](LICENSE). See the LICENSE file for more details.

### Contact

For questions or feedback, please contact [Nithesh K](https://www.linkedin.com/in/mrnithesh/).
