with open ("Notes.txt", "w") as f:
    f.write("My Name is Abu Akasha.\n")
    f.write("I'm Learning python on self based study.\n")
    f.write("My goal is to become an AI engineer.\n")

print("Your notes.txt file is created!")

# Write multiple line at once
lines = ["line 1\n", "line 2\n", "line 3\n"]
with open("line.txt", "w") as f:
    f.writelines(lines)

print("Lines file ready!")