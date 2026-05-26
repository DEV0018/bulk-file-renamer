import os

files = os.listdir(".")

prefix = input("Enter new filename prefix: ")

count = 1

for file in files:

    # Skip folders and Python file
    if os.path.isdir(file) or file == "renamer.py":
        continue

    # Split extension
    filename, extension = os.path.splitext(file)

    # Create new filename
    new_name = f"{prefix}_{count}{extension}"

    # Rename file
    os.rename(file, new_name)

    print(f"Renamed {file} → {new_name}")

    count += 1