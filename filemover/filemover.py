import os

source = "C:\\Users\\dvillalva\\Desktop\\scripts_from_x\\filemover\\test.txt"
destination = "C:\\Users\\dvillalva\\Desktop\\test.txt"

try:
    if os.path.exists(destination):
        print("There is already a file there")
    else:
        os.replace(source,destination)
        print(source+" was moved")
except FileNotFoundError:
    print(source+" was not found")