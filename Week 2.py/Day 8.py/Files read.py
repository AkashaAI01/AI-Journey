# Read full file 
with open ("Notes.txt", "r") as f:
    content = f.read()
    print(content)

# Read the file line by line 
with open ("Notes.txt", "r") as f:
    for line in f:
        print(line.strip())

# Read in lists
with open ("Notes.txt", "r") as f:
    lines = f.readlines()
    print(f"Total lines: {len(lines)}")
    print(f"First line: {lines[0].strip()}")