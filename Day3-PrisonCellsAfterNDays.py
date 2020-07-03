from typing import List


class PrisonCells:
    def prisonAfterNDays(self, cells: List[int], N: int) -> List[int]:
        N = ((N - 1) % 14) + 1
        for i in range(N):
            temp = [0] * len(cells)
            for j in range(1, len(cells) - 1):
                if cells[j - 1] == cells[j + 1]:
                    temp[j] = 1
            cells = temp[:]
        return cells


obj = PrisonCells()
print(obj.prisonAfterNDays([0, 1, 0, 1, 1, 0, 0, 1], 7))
print(obj.prisonAfterNDays([0, 1, 0, 1, 1, 0, 0, 1], 100000))
print(obj.prisonAfterNDays([0, 1, 0, 1, 1, 0, 0, 1], 574))
