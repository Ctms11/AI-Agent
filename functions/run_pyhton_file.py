import os
import subprocess
def run_python_file(working_directory, file_path, args=None):
    working_dir_abs = os.path.abspath(working_directory)
    target_dir = os.path.normpath(os.path.join(working_dir_abs, file_path)) 
    valid_target_dir = os.path.commonpath([working_dir_abs, target_dir]) == working_dir_abs
    try:
        if valid_target_dir is False:
            return f'Error: Cannot execute "{file_path}" as it is outside the permitted working directory'
        if os.path.isfile(target_dir) is False:
            return f'Error: "{file_path}" does not exist or is not a regular file'
        if target_dir.endswith(".py") is False:
            return f'Error: "{file_path}" is not a Python file'
        command = ['python', target_dir]
        if args:
            command.extend(args)
        result = subprocess.run(command, capture_output=True,text=True, timeout=30)
        if result.returncode != 0:
            return f"Process exited with code {result.returncode}"
        elif result.stdout is None or result.stderr is None:
            return f"No output produced"
        else:
            return f'STDOUT:\n{result.stdout}\nSTDERR:\n{result.stderr}'
    except Exception as e:
        return f'Error: executing Python file:{e}'
        