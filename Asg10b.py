class B:
    def __init__(self, val1: int):
        self.val1 = val1
        print("Class B Object Created")

    def show(self):
        print(f"Showing class B object having value {self.val1}")


b = B(10)
b.show()
