from google.genai import types
from functions.get_file_info import schema_get_files_info 
from functions.write_to_file import schema_write_to_file
from functions.run_pyhton_file import schema_run_python_file
from functions.get_file_content import schema_get_file_content

available_functions = types.Tool(
    function_declarations=[schema_get_files_info, schema_get_file_content, schema_write_to_file, schema_run_python_file],
)