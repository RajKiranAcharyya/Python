def isprime(num):
    if num < 2:
        return False
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            return False
    return True


def generateprimes(n):
    primes = []
    current = 2
    while len(primes) < n:
        if isprime(current):
            primes.append(current)
        current += 1
    return primes


def write_primes_to_file(filename, primes):
    with open(filename, "w") as file:
        for prime in primes:
            file.write(str(prime) + " ")


n = int(input("Enter The Number Of Prime Numbers To Store: "))
filename = "prime_numbers.txt"
primes = generateprimes(n)
write_primes_to_file(filename, primes)
print(f"The first {n} prime numbers have been written to {filename}")
