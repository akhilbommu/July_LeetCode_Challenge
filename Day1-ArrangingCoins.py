class ArrangingCoins:
    def arrangeCoins(self, n: int) -> int:
        i = 0
        while i < n:
            i += 1
            n = n - i
        return i


obj = ArrangingCoins()
print(obj.arrangeCoins(5))
print(obj.arrangeCoins(8))