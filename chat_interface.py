import gradio as gr
from dotenv import load_dotenv
from langchain_openai import ChatOpenAI
from langchain.schema import AIMessage, HumanMessage, SystemMessage
from config import LLM_MODEL, GRADIO_TITLE, SYSTEM_MESSAGE
from extraction_module import extract_py_files

def launch_chat_interface(folder):
    """
    Launches the Gradio chat interface. The code context is extracted from the provided folder.
    """
    # Extract the complete code context (folder schema and file contents)
    CODE_CONTEXT = extract_py_files(folder)
    system_message_with_context = f"{SYSTEM_MESSAGE}\n{CODE_CONTEXT}"

    load_dotenv()

    # Initialise the LLM using LangChain's OpenAI integration.
    llm = ChatOpenAI(
        model_name=LLM_MODEL,
        temperature=0,
    )

    def generate_response(user_message, chat_history):
        """
        Generates a response by sending a prompt to the LLM that includes the code context and the user's message.
        """

        history_langchain_format = [SystemMessage(content=system_message_with_context)]

        for msg in chat_history:
            if msg['role'] == 'user':
                history_langchain_format.append(HumanMessage(content=msg['content']))
            elif msg['role'] == 'assistant':
                history_langchain_format.append(AIMessage(content=msg['content']))

        history_langchain_format.append(HumanMessage(content=user_message))

        ai_response = llm.invoke(history_langchain_format)

        # Update the chat history with the new messages.
        chat_history.append({'role': 'user', 'content': user_message})
        chat_history.append({'role': 'assistant', 'content': ai_response.content})

        return '', chat_history

    # Create a simple chat interface using Gradio Blocks.
    CSS = """
    /* This ensures the second column fills the viewport height */
    #second_column { 
        height: 100vh; 
        display: flex;
        flex-direction: column;
    }
    /* This makes the chatbot fill the available space within its column */
    #chatbot { 
        flex-grow: 1; 
        overflow: auto;
    }
"""

    with gr.Blocks(css=CSS) as demo:

        with gr.Row(scale=1):
            with gr.Column(scale=1):  # Left column: one third of the width
                gr.Markdown("## Your Title Here")
                user_input = gr.Textbox(placeholder="Enter your message here...", label="Your message")
            with gr.Column(scale=2, elem_id="second_column"):  # Right column: two thirds of the width
                chatbot = gr.Chatbot(type='messages', elem_id="chatbot")
        state = gr.State([])

        user_input.submit(generate_response, inputs=[user_input, state], outputs=[user_input, chatbot])

    demo.launch(debug=True)


if __name__ == "__main__":
    # For testing purposes you might set a default folder or pass one via command-line.
    folder_path = "path/to/your/folder"  # Replace with your folder path or use command-line arguments.
    launch_chat_interface(folder_path)
