l = []
print(l)  # []

l1 = ["Apple", "Banana", "Orange"]  # ['Apple', 'Banana', 'Orange']
print(l1)

tupple = ("a", "b", "C")  # ('a', 'b', 'C')
print(tupple)

l2 = list(tupple)
print(l2)  # ['a', 'b', 'C']

for i in range(len(l2)):
    print(l2[i])  # a
    # b
    # C

for i in l2:
    print(i)  # a
    # b
    # C

for i in range(len(l2)):
    l2.append(i**2)  # ['a', 'b', 'C', 0, 1, 4]
print(l2)

print(l2[:5])  # ['a', 'b', 'C', 0, 1]
print(l2[-5:])  # ['b', 'C', 0, 1, 4]
print(l2[:-1])  # ['a', 'b', 'C', 0, 1]