a = input("Enter A Statement: ")
uppercase = 0
lowercase = 0
for i in range(len(a)):
    if a[i] >= "A" and a[i] <= "Z":
        uppercase = uppercase + 1
    elif a[i] >= "a" and a[i] <= "z":
        lowercase = lowercase + 1
    else:
        continue
print(uppercase," ",lowercase)
