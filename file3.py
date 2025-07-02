import os
directory_path ='/'
# List all files and directories in the current directory
contents = os.listdir(directory_path)
print("Contents of current directory:")

for i in contents:
 print(i)