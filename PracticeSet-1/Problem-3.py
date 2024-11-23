import os

# specify the directory you want to list
diractory_path = '/VS_codes'

# List all files and directories in the specified path
contents = os.listdir(diractory_path)

# print each file and directory name
for item in contents:
    print(item)