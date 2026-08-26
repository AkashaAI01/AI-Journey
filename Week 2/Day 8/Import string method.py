text = " Hello Pakistan! "

# Clean white space
print(text.strip())
print(text.lstrip())

# change case 
print(text.strip().upper())
print(text.strip().title())

# Search and replace
print(text.replace("Pakistan", "Akasha"))

# split into list 
sentence = "Apple,mango,bnana"
fruits = sentence.split(",")
print(fruits)

# list joining into string 
print(" | ".join(fruits))

# Check content
print("Hello".startswith("He"))
print("Hello".endswith("ll"))
print("Pakistan" in text) 