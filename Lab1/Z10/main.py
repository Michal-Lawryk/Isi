import random
con = True
ans = random.randint(1, 100)
counter = 0
while con:
    guess = int(input())
    if guess > ans:
        print("Za duża")
        counter += 1
    elif guess < ans:
        print("Za mała")
        counter += 1
    else:
        counter += 1
        con = False

print("Wygrałeś!")
print("Ilość prób:", counter)
