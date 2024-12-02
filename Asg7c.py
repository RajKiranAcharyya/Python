def primeCheck(n):
    if n <= 1:
        return False
    for i in range(2, int(n ** (0.5) + 1)):
        if n % i == 0:
            return False
    return True


PrimeList = tuple(filter(primeCheck, range(5500, 250, -1)))
print("All Prime Numbers Between 251 to 5500 Are:", PrimeList)
