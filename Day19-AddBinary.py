class AddBinary:
    def addBinary(self, a: str, b: str) -> str:
        return str(bin(int(a,2) + int(b,2))[2:])


obj = AddBinary()
print(obj.addBinary("11", "1"))
print(obj.addBinary("1010", "1011"))