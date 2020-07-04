class UglyNumber2:
    def nthUglyNumber(self, num: int) -> int:
        results = [1]
        i, j, k, count = 0, 0, 0, 0
        while count < num:
            temp = min(results[i] * 2, min(results[j] * 3, results[k] * 5))
            if temp == results[i] * 2:
                i += 1
            if temp == results[j] * 3:
                j += 1
            if temp == results[k] * 5:
                k += 1
            count += 1
            if count == num:
                return results[-1]
            results.append(temp)


obj = UglyNumber2()
print(obj.nthUglyNumber(10))
print(obj.nthUglyNumber(100))