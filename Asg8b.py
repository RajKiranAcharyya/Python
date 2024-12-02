import numpy as np
from random import randint

a = []
b = []

r = int(input("Enter The No. Of Rows: "))
c = int(input("Enter The No. Of Coloums: "))

print("Input Matrix A")
for i in range(r):
    m = []
    for j in range(c):
        m.append(int(input()))
    a.append(m)

print(f"Matrix A={a}")

print("Matrix B Is Being Input Randomly")
for i in range(c):
    m = []
    for j in range(r):
        m.append(randint(1, 21))
    b.append(m)

print(f"Matrix B={b}")

c = np.dot(a, b)
print(f"Matrix C={c}")
