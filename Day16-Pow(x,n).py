class Power:
    def myPow(self, x: float, n: int) -> float:
        return pow(x, n)


obj = Power()
print(obj.myPow(2.00000, 10))
print(obj.myPow(2.10000, 3))
print(obj.myPow(2.00000, -2))
