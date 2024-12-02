if __name__ == '__main__':
    s = input()
    checks = [False] * 5  # [alnum, alpha, digit, lower, upper]

    for char in s:
        if char.isalnum():
            checks[0] = True
        if char.isalpha():
            checks[1] = True
        if char.isdigit():
            checks[2] = True
        if char.islower():
            checks[3] = True
        if char.isupper():
            checks[4] = True

    # Output the results
    print("True" if checks[0] else "False")  # Alphanumeric
    print("True" if checks[1] else "False")  # Alphabetical
    print("True" if checks[2] else "False")  # Digits
    print("True" if checks[3] else "False")  # Lowercase
    print("True" if checks[4] else "False")  # Uppercase
