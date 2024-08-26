def read_text_dir(dir_path):
    import os
    from pathlib import Path

    dir_path = Path(dir_path)

    # Validate that the path exists and is a directory
    if not dir_path.exists():
        raise FileNotFoundError(f"The directory '{dir_path}' does not exist.")
    if not dir_path.is_dir():
        raise NotADirectoryError(f"The path '{dir_path}' is not a directory.")

    # Get the list of files in the directory
    file_ls = os.listdir(dir_path)

    # Construct full file paths
    path_ls = [dir_path / file for file in file_ls]

    # Read contents of each file, with error handling
    content_dict = {}
    for file, path in zip(file_ls, path_ls):
        try:
            content_dict[file] = read_text_file(path)
        except Exception as e:
            print(f"Error reading file '{file}': {e}")
            continue
    # Sort the dictionary by keys
    sorted_content_dict = dict(sorted(content_dict.items()))
    return sorted_content_dict



def read_text_file(file_path):
    from pathlib import Path
    
    file_path = Path(file_path)
    try:
        # Open the text file in read mode
        with open(file_path, 'r', encoding='utf-8') as file:
            # Read the entire file content into a string
            text_content = file.read()
            return text_content
    except FileNotFoundError:
        print(f"The file {file_path} was not found.")
    except Exception as e:
        print(f"An error occurred: {e}")
