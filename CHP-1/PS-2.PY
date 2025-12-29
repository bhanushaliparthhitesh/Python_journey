import os

# specify the directory you want to list
directory_path = "/"

try:
    # get the list of files and folders
    contents = os.listdir(directory_path)

    # print each item
    for item in contents:
        print(item)

except FileNotFoundError:
    print(f"The directory {directory_path} was not found.")
except PermissionError:
    print(f"Permission denied to access {directory_path}.")
except Exception as e:
    print(f"An error occurred: {e}")
