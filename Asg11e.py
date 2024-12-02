import os


def get_file_size(filename):
    try:
        s = os.path.getsize(filename)
        print(f"The Size Of {filename} Is {s} bytes")
    except FileNotFoundError:
        print(f"The File {filename} Does Not Exist")
    except Exception as e:
        print(f"An Error Occured{e}")


filename = input("Enter The File Name Which Size You Want To See: ")
get_file_size(filename)
