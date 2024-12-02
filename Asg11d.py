# charcteristics of oops
# built in exception handling error
# define module,package
# data abstruction
# what is class


def read_and_display(filename):
    try:
        with open(filename, "r") as file:
            lines = file.readlines()
            print("Contents Of File: ")
            for line in lines:
                print(line.strip())
    except FileNotFoundError as e:
        print(f"An Error Occured {e}")


filename = input("Enter The File Name Which You Want To Read: ")
read_and_display(filename)
