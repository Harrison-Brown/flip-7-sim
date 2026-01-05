class NumberedCard:
    def __init__(self, number):
        self.number = number

    def __str__(self):
        return str(self.number)
    
    def __eq__(self, other):
        if isinstance(other, NumberedCard):
            return self.number == other.number
        raise TypeError("Comparison is only supported between NumberedCard instances.")
    
    