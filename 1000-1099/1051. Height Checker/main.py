from typing import List


class Solution:
    def heightChecker(self, heights: List[int]) -> int:
        expected = sorted(heights)
        result = sum(1 for item_1, item_2 in zip(heights, expected) if item_1 != item_2)

        return result


result = Solution().heightChecker([1, 1, 4, 2, 1, 3])
print(result)
