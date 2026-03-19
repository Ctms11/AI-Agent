import os
from google.genai import types
def get_file_content(working_directory, file_path):
    char_len = 10000
    working_dir_abs = os.path.abspath(working_directory)
    target_file = os.path.normpath(os.path.join(working_dir_abs, file_path)) 
    valid_target_file = os.path.commonpath([working_dir_abs, target_file]) == working_dir_abs
    try:
        if valid_target_file is False:
            return f'Error: Cannot read "{file_path}" as it is outside the permitted working directory'
        if not os.path.isfile(target_file):
            return f'Error: "{file_path}" is not a file'
        with open(target_file, 'r') as f:
            file_content_string = f.read(char_len) 
           # After reading the first MAX_CHARS...
            if len(f.read()) > char_len:
                return file_content_string + "\n" + f'[...File "{file_path}" truncated at {char_len} characters]'
            return file_content_string
    except Exception as e:
        return f'Error: {e}'
    

schema_get_file_content = types.FunctionDeclaration(
    name="get_files_content",
    description="Lists files in a specified directory relative to the working directory, providing file size and directory status",
    parameters=types.Schema(
        type=types.Type.OBJECT,
        properties={
            "directory": types.Schema(
                type=types.Type.STRING,
                description="Directory path to read the file from, relative to the working directory (default is the working directory itself)",
            ),
        },
    ),
)    