def fibo(n):
    if n == 1:
        return 0
    elif n == 2:
        return 1
    else:
        return fibo(n - 1) + fibo(n - 2)


a = int(input("Enter The No. Of Term: "))
print(f"The {a}th Term Of The Fibonacci Series Is:",fibo(a))