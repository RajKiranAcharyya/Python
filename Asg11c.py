fibonacci = []


def fibo(a, b, n):
    if n > 0:
        fibonacci.append(a)
        fibo(b, a + b, n - 1)


n = int(input("Enter The Term: "))
fibo(0, 1, n)
filename = "fibonacci_numbers.txt"
with open(filename, "w") as file:
    for f in fibonacci:
        file.write(str(f) + " ")


print(f"fibonacci numbers has been written to {filename}")
