import os
from google import genai
from google.genai import types
def get_files_info(working_directory, directory="."):
    working_dir_abs = os.path.abspath(working_directory)
    target_dir = os.path.normpath(os.path.join(working_dir_abs, directory)) 
    valid_target_dir = os.path.commonpath([working_dir_abs, target_dir]) == working_dir_abs
    try:
        if valid_target_dir is False:
            return f'Error: Cannot list "{directory}" as it is outside the permitted working directory'
        if not os.path.isdir(target_dir):
            return f'Error: "{directory}" is not a directory'
        lines = []
        for target in os.listdir(target_dir):
            target_path = os.path.join(target_dir, target)
            lines.append(f"- {target}: file_size={os.path.getsize(target_path)} bytes, is_dir={os.path.isdir(target_path)}")
        return "\n".join(lines)
    except Exception as e:
        return f'Error: {e}'


schema_get_files_info = types.FunctionDeclaration(
    name="get_files_info",
    description="Lists files in a specified directory relative to the working directory, providing file size and directory status",
    parameters=types.Schema(
        type=types.Type.OBJECT,
        properties={
            "directory": types.Schema(
                type=types.Type.STRING,
                description="Directory path to list files from, relative to the working directory (default is the working directory itself)",
            ),
        },
    ),
)    
        
    
    
        


    

    