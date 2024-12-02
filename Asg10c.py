class B:
    def __init__(self, val1: int):
        self.val1 = val1

    def show(self):
        print(f"Showing class B object having value {self.val1}")


class C(B):
    def __init__(self, val1: int, val2: int):
        super().__init__(val1)  # super = superior
        self.val2 = val2
        print("Class C object created")

    def show(self):
        print(f"Showing Class C with {self.val1},{self.val2}")


c = C(10, 20)
c.show()
