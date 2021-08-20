um_counter = 0
like_counter = 0

# Text-to-Speech File Name
text_file = input("File Name: ")

# Open File + Read
with open("%s" % text_file) as monologue:
    monologue = monologue.readlines()


for words in monologue:
    list_words = words.split()

# Count how many "um" & "like" words
for word in list_words:
    if word == "um":
        print(word)
        um_counter += 1
    elif word == "like":
        print(word)
        like_counter += 1

# Print total count
print("UM counter =", um_counter)
print("LIKE counter =", like_counter)
