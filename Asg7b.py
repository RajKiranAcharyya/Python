def fibo(a, b, n):                    # a= n-1      b=n-2
    if n > 0:
        print(a, end=" ")
        fibo(b, a + b, n - 1)


a = int(input("Enter The No. Of Term: "))
print(f"The Fibonacci Series Upto {a}: ",end="")
fibo(0, 1, a)
