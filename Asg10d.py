class A:
    def __init__(self, val1=None):
        self.val1 = val1
        print(f"Class A initialized with value:{self.val1}")


class B:
    def __init__(self, val1=None):
        self.val1 = val1
        print(f"Class A initialized with value:{self.val1}")


class E(A, B):
    def __init__(self, *args):
        if len(args) == 0:
            super().__init__()
            print("Class E object created")
        elif len(args) == 1:
            super().__init__(args[0])
            print("Class E object created with one value")
        else:
            raise ValueError("Class E can only be created with 0 or 1 argument()")

    def show(self):
        if not hasattr(self, "val1"):
            print("Show Class E")
        else:
            print(f"Showing class E with value{self.val1}")


e1 = E()
e1.show()
e2 = E(10)
e2.show()
