import os

directory = input("Enter the directory path where files need to be renamed: ")
new_name = input("Enter the new name for files: ")

i = 1

for filename in os.listdir(directory):
    file_extension = os.path.splitext(filename)[1]
    new_filename = f"{new_name}{i}{file_extension}"
    source = os.path.join(directory, filename)
    destination = os.path.join(directory, new_filename)
    os.rename(source, destination) 
    i += 1
print("Files renamed successfully!")
