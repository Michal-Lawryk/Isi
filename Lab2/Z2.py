f = open("test.txt", "r")
string = f.read()
string = string.replace("(", "")
string = string.replace(")", "")
string = string.replace("?", "")
string = string.replace(".", "")
string = string.replace(",", "")
max_string = ""
for word in string.split():
    if len(word) > len(max_string):
        max_string = word
print("The longest word in text:", max_string)
f.close()