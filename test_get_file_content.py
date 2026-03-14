from functions.get_file_content import get_file_content

print(get_file_content("calculator", "lorem.txt")+"\n\n")
print(get_file_content("calculator", "main.py")+"\n\n")
print(get_file_content("calculator", "pkg/calculator.py")+"\n\n")
print(get_file_content("calculator", "/bin/cat")+"\n\n")
print(get_file_content("calculator", "pkg/does_not_exist.py")+"\n\n")