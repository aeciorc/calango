class Token:
    def __init__(self, value, kind):
        self.value = value
        self.kind = kind

    def __str__(self):
        return self.value

    def __repr__(self):
        return self.value


