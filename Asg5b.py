a = input("Enter Your EMAIL ID: ")
j_not_atr = 0
for i in range(len(a)):
    if a[i] == ".":
        break
    elif a[i] != "@" and j_not_atr == 0:
        print(a[i], end="")
    elif a[i] == "@":
        j_not_atr = 1
        print(end=" ")
    else:
        print(chr(ord(a[i]) - 32), end="")