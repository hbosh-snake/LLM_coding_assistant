import os
from config import SKIP_FOLDERS


def build_folder_schema(root_folder):
    """
    Builds a text-based schema of the folder structure starting at root_folder,
    including only folders and .py files, while skipping folders specified in SKIP_FOLDERS.
    """
    tree_lines = []
    root_folder = os.path.abspath(root_folder)
    for current_root, dirs, files in os.walk(root_folder):
        # Remove directories listed in SKIP_FOLDERS to prevent recursing into them
        dirs[:] = [d for d in dirs if d not in SKIP_FOLDERS]

        # Compute the relative path and indentation level for a tree-like schema
        rel_path = os.path.relpath(current_root, root_folder)
        indent_level = 0 if rel_path == '.' else rel_path.count(os.sep) + 1
        folder_name = os.path.basename(current_root) if rel_path != '.' else os.path.basename(root_folder)
        tree_lines.append("    " * (indent_level - 1) + f"{folder_name}/")

        # Sort files to ensure a consistent order and list only .py files
        for file in sorted(files):
            if file.endswith(".py"):
                tree_lines.append("    " * indent_level + file)
    return "\n".join(tree_lines)


def extract_py_files(root_folder):
    """
    Recursively reads all .py files in root_folder and its subfolders, excluding folders in SKIP_FOLDERS.
    Returns a string that starts with a folder schema followed by each file's content,
    each preceded by a minimal header with its relative file path.
    """
    folder_schema = build_folder_schema(root_folder)
    file_contents = []
    root_folder = os.path.abspath(root_folder)

    for current_root, dirs, files in os.walk(root_folder):
        # Skip folders defined in SKIP_FOLDERS
        dirs[:] = [d for d in dirs if d not in SKIP_FOLDERS]

        for file in sorted(files):
            if file.endswith(".py"):
                file_path = os.path.join(current_root, file)
                # Get relative file path for a concise header
                rel_file_path = os.path.relpath(file_path, root_folder)
                with open(file_path, "r", encoding="utf-8") as f:
                    code = f.read()
                # Minimal header: "#F:<relative file path>"
                file_contents.append(f"#F:{rel_file_path}\n{code}")

    # Combine the folder schema and all file contents
    full_content = f"Folder Structure:\n{folder_schema}\n\n" + "\n\n".join(file_contents)
    return full_content


# Example usage:
if __name__ == "__main__":
    folder_path = r"C:\Users\Emanuele\PycharmProjects\CEMS_Mapping_LLM"  # Replace with your actual folder path
    content = extract_py_files(folder_path)
    print(content)
