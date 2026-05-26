# ✏️ Bulk File Renamer using Python

A Python automation project that automatically renames multiple files using custom filename prefixes while preserving original file extensions.

---

# 🚀 Features

✅ Rename multiple files automatically
✅ Supports all file types
✅ Preserves original file extensions
✅ User can choose custom filename prefixes
✅ Skips folders automatically
✅ Beginner-friendly automation project

---

# 🛠️ Technologies Used

* Python
* os module

---

# 📁 Example

## Before Running

```text
project-folder/
│
├── img1.jpg
├── img2.jpg
├── notes.pdf
├── song.mp3
└── renamer.py
```

## After Running

Input:

```text
vacation
```

Output:

```text
project-folder/
│
├── vacation_1.jpg
├── vacation_2.jpg
├── vacation_3.pdf
├── vacation_4.mp3
└── renamer.py
```

---

# ▶️ How to Run the Project

## Step 1

Clone the repository:

```bash
git clone https://github.com/your-username/bulk-file-renamer.git
```

## Step 2

Open the project folder:

```bash
cd bulk-file-renamer
```

## Step 3

Run the Python script:

```bash
python renamer.py
```

---

# 📜 Project Code

```python
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
```

---

# 🧠 Concepts Learned

* Python Automation
* File Handling
* os Module
* Loops and Conditions
* User Input
* Batch Processing



