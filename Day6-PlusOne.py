from typing import List


class PlusOne:
    def plusOne(self, digits: List[int]) -> List[int]:
        list_str = list(map(str,digits))
        string = ''.join(list_str)
        res = int(string) + 1
        res_str = str(res)
        res_list = list(map(int,res_str))
        return res_list

obj = PlusOne()
print(obj.plusOne([1,2,3]))
print(obj.plusOne([4,3,2,1]))
print(obj.plusOne([9]))