class InnerBag:
    def __init__(self, amount: int, name: str):
        self.amount = amount
        self.name = name

    def __eq__(self, other):
        if not isinstance(other, InnerBag):
            return NotImplemented

        return self.amount == other.amount and self.name == other.name
