class HammingDistance:
    def hammingDistance(self, x: int, y: int) -> int:
        xor_ = x ^ y
        return bin(xor_).count('1')


obj = HammingDistance()
print(obj.hammingDistance(1,4))