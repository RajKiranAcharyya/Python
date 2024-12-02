filename = "Welcome.txt"
with open(filename, "w") as file:
    file.write("Welcome To Python")
print(f'Text "Welcome To Python" has been written to {filename}')
