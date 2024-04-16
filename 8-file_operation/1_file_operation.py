# File Creation and Writing

# Open a file in write mode ('w'). If the file does not exist, it will be created.
# If the file exists, it will be truncated, meaning its previous contents will be deleted.
with open("example.txt", "w") as file:
    # Write to the file using the write() method.
    file.write("Hello, world!\n")
    file.write("This is a sample file created using Python.\n")

# File Reading

# Open the file in read mode ('r').
with open("example.txt", "r") as file:
    # Read the entire contents of the file using the read() method.
    content = file.read()
    print("File Contents:")
    print(content)

# File Appending

# Open the file in append mode ('a'). If the file does not exist, it will be created.
# If the file exists, the new content will be appended to the end of the file.
with open("example.txt", "a") as file:
    # Append additional content to the file.
    file.write("Appending new content to the file.\n")

# File Reading Line by Line

# Open the file in read mode ('r').
with open("example.txt", "r") as file:
    # Read the file line by line using a loop.
    print("File Contents (Line by Line):")
    for line in file:
        print(line.strip())  # Use strip() to remove newline characters.

# File Handling Errors

try:
    # Attempt to open a non-existent file in read mode ('r').
    with open("non_existent_file.txt", "r") as file:
        content = file.read()
        print(content)
except FileNotFoundError:
    print("File not found!")

# File Closing (Explicitly)

# It's good practice to close files explicitly, although using "with" statement handles it automatically.
file = open("example.txt", "r")
try:
    content = file.read()
    print(content)
finally:
    file.close()
