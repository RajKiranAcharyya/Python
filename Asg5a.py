a = input("Enter A String: ")
a=list(a)
for i in range(len(a)):
    if a[i] >= "A" and a[i] <= "Z":
        a[i] = chr(ord(a[i]) + 32)
    elif a[i] >= "a" and a[i] <= "z":
        a[i] = chr(ord(a[i]) - 32)
a = ''.join(a)
print(a)