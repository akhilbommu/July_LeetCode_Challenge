from typing import List


class Subsets:

    def generateSubsets(self, index, nums, current, subsets):
        temp = current[:]
        subsets.append(temp)
        for i in range(index, len(nums)):
            current.append(nums[i])
            self.generateSubsets(i + 1, nums, current, subsets)
            current.pop(-1)

    def subsets(self, nums: List[int]) -> List[List[int]]:
        subsets = []
        self.generateSubsets(0, nums, [], subsets)

        return subsets


obj = Subsets()
print(obj.subsets([1, 2, 3]))