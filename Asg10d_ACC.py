class F:
    def __init__(self, string):
        self.string = string

    def __sub__(self, other):
        result = "".join([char for char in self.string if char not in other.string])
        return result
                        # """char is used as a variable,which is keeping track for the
                        #                        current value of self.string with the other.string"""


x = F("abcdef")
y = F("bdfh")

print(x - y)
