f = int(input("Enter The Number of Fibonacci Terms: "))
a = 0
b = 1
print("Fibonacci Series:", end=" ")
for i in range(0, f + 1):
    if i < 2:
        print(i, end=" ")
    else:
        sum = a + b
        print(sum, end=" ")
        a = b
        b = sum
