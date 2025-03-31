import argparse
from chat_interface import launch_chat_interface


def main():
    parser = argparse.ArgumentParser(description="Launch the chat interface for analysing Python code.")
    parser.add_argument("folder", help="Folder to analyse")
    args = parser.parse_args()

    # Launch the chat interface using the provided folder
    launch_chat_interface(folder=args.folder)


if __name__ == "__main__":
    main()
