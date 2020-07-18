import operator
from collections import OrderedDict
from typing import List


class TopKFrequentElements:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        res_list = []
        d = OrderedDict()
        nums_set = set(nums)
        for each in nums_set:
            d[each] = nums.count(each)
        print(d)
        sorted_d = sorted(d.items(), key=operator.itemgetter(1), reverse=True)
        print(sorted_d)
        for each in sorted_d:
            if k > 0:
                res_list.append(each[0])
            k -= 1
        return res_list


obj = TopKFrequentElements()
print(obj.topKFrequent([1, 1, 1, 2, 2, 3], 2))
print(obj.topKFrequent([1], 1))