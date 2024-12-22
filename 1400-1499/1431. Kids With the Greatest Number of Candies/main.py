from typing import List


class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        candy_max = max(candies)
        result = [
            True if (candy + extraCandies >= candy_max) else False for candy in candies
        ]

        return result


result = Solution().kidsWithCandies([2, 3, 5, 1, 3], 3)
print(result)
