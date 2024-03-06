text = input()
text = text.replace(" ", "").lower()
reverse = text[::-1]
flag = True
for x in range(len(text)):
    if text[x] != reverse[x]:
        flag = False
if flag:
    print("Wyraz jest palindromem")
else:
    print("Wyraz nie jest palindromem")
