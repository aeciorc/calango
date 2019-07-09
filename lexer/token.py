class Token:
    def __init__(self, value, kind):
        self.value = value
        self.kind = kind

    def __eq__(self, other):
        return self.value == other.value and self.kind == other.kind

    def __str__(self):
        return self.value

    def __repr__(self):
        return "{},{}".format(self.value, self.kind)
