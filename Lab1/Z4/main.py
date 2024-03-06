counter = 0
for x in range(100):
    if x % 3 == 0 and x % 4 == 0:
        counter += 1
        print(x)
print("Counter: ", counter)
