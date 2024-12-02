import numberCheck

a = int(input("Enter A Number: "))
print(
    f"\n{a} Is Prime: {numberCheck.is_prime(a)}\n{a} Is Palindrome: {numberCheck.is_palindrome(str(a))}"
)
