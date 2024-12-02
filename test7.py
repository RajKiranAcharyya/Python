def sum(a, b):
    return a + b


print(sum(4, 5))


def myfun(x, y=9):
    print("x=", x)
    print("y=", y)


myfun(100)


def student(firstname, middlename, lastname):
    print("Name:", firstname + middlename + lastname)


student("Raj ", "Kiran ", "Acharyya")


seq = [
    0,
    8,
    9,
    101,
    2,
    3,
    4,
    5,
    6,
    7,
]
print(seq)
result = filter(lambda x: x % 2 != 0, seq)
print(list(result))
result = filter(lambda x: x % 2 == 0, seq)
print(list(result))
