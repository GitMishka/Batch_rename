import os
directory = input("Enter the directory path where files need to be renamed: ")
prefix = input("Enter the prefix to be added: ")



# Rename the files
for filename in os.listdir(directory):
    new_filename = prefix + filename
    source = os.path.join(directory, filename)
    destination = os.path.join(directory, new_filename)
    
    os.rename(source, destination)  # rename the file

print("Files renamed successfully!")
