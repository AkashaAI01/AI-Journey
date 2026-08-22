import os

# Apeend mood, In this mood the previos content will saf.
with open ("log.txt", "a") as f:
    f.write("New entry added! \n")

# File checking wether it is available or not.
if os.path.exists("log.txt"):
    print("File exists.")
    with open ("log.txt", "r") as f:
        print(f.read())
else:
    print("File dosn't exists.")