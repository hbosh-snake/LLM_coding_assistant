# List of folder names to skip during the file search.
SKIP_FOLDERS = [".venv", "build", "dist", ".git", ".idea", ".env"]

# LLM configuration
LLM_MODEL = "gpt-4o-mini"

# Gradio interface configuration
GRADIO_TITLE = "Code Assistant Chat"

CODE_FOLDER_PATH = ""

SYSTEM_MESSAGE = """I am sharing my entire python code below, starting with the code structure.
Depending on what I ask next, please respond accordingly by either rewriting functions,
providing code snippets, offering suggestions, or debugging error messages.
When your answer includes code, wrap it in triple backticks (```), and do not include any additional explanation 
unless I specifically request it.
For example, if I ask for a rewritten function, return only the complete function inside a code block.
If I share an error message along with my code, provide debugging advice and any necessary code changes—again, 
with all code formatted in triple backticks.
If I ask you to explain what the code does, adjust your explanation to the level of difficulty I request.
I might ask about the whole code or just a specific function.
You will be especially useful when rewriting parts of the code 
while considering the broader context of the entire script.
Here is my code:"""
