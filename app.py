class Calculator:

    def __init__(self, a=0, b=9) -> None:
        self.a = a
        self.b = b

    def addition(self) -> int:
        return self.a + self.b

    def subtraction(self) -> float:
        return self.a - self.b

    def multiplication(self) -> float:
        return self.a * self.b

    def division(self) -> float:
        return self.a / self.b


        