# LLM Coding Assistant

This project is a simple Python-based coding assistant that leverages a language model to help users analyse and interact with Python code. It provides a chat interface where users can ask questions, receive suggestions, and obtain relevant code snippets.

The assistant reads all `.py` files from a specified folder and its subfolders, compiles their contents into a single string, and sends it as a system message to a language model, enabling interactive, chat-based support.

## Folder Structure
LLM_coding_assistant
├── chat_interface.py
├── config.py
├── extraction_module.py
├── main.py
└── pycache/


## Features

- **Chat Interface**: A user-friendly interface built with Gradio for real-time interaction.
- **Code Context Extraction**: Automatically extracts Python files and their contents from a specified folder.
- **LLM Integration**: Utilizes OpenAI's language model to generate responses based on user queries and code context.

## Requirements

- Python 3.x
- Gradio
- LangChain
- OpenAI API key (for LLM usage)
- `python-dotenv` (for loading environment variables)

## Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/yourusername/LLM_coding_assistant.git
   cd LLM_coding_assistant

Install the required packages:

pip install -r requirements.txt
Set up your OpenAI API key in a .env file:

OPENAI_API_KEY=your_api_key_here

## Usage

To launch the chat interface, run the following command in your terminal:


python main.py path/to/your/folder

Replace path/to/your/folder with the path to the folder containing your Python files.

## Contributing
Contributions are welcome! Please feel free to submit a pull request or open an issue for any suggestions or improvements.

## License
This project is licensed under the MIT License - see the LICENSE file for details.