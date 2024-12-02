a = [1, 5, 2]
for i in range(len(a)):
    key = a[i]
    j = i - 1
    while j > -1 and a[j] > key:
        a[j + 1] = a[j]
        j = j - 1
    a[j + 1] = key
print(a)
b = [0] * (a[len(a) - 1] + 1)
# b[a[0]] = a[0]
# b[a[1]] = a[1]
# b[a[2]] = a[2]
for i in a:
    b[i]=i
print(b)
