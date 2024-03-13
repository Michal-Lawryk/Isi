import random
import string

f = open("passwords.txt", "w")
new_pass = ""
characters = string.ascii_letters + string.digits
for x in range(1000):
    new_pass += "".join(random.choice(characters) for i in range(6))
    new_pass += "\n"
f.write(new_pass)
f.close()
