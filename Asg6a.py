# Using Shortcurt

a = [10, 11, 100, 200, 300, 34]
a.sort()
print(a[1], a[len(a) - 2])       #11 200


# Without Using Shortcurt

b = [10, 11, 100, 200, 300, 34]
for i in range(len(b)):
    key = b[i]
    j = i - 1
    while j > -1 and b[j] > key:
        b[j + 1] = b[j]
        j = j - 1
    b[j + 1] = key
print(b[1], b[len(b) - 2])       #11 200