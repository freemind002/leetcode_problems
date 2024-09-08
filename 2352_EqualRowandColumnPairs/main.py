from collections import Counter
from typing import List


class Solution:
    def equalPairs(self, grid: List[List[int]]) -> int:
        cnt = Counter(tuple(row) for row in grid)
        result = sum([cnt[tpl] for tpl in zip(*grid)])

        return result


result = Solution().equalPairs(
    grid=[[3, 1, 2, 2], [1, 4, 4, 4], [2, 4, 2, 2], [2, 5, 2, 2]]
)
print(result)
