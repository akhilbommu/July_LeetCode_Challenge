class ReverseBits:
    def reverseBits(self, n: int) -> int:
        return str(n)[::-1]


obj = ReverseBits()
print(obj.reverseBits(11111111111111111111111111111101))
