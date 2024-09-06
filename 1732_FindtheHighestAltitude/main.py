import itertools
from typing import List


class Solution:
    def largestAltitude(self, gain: List[int]) -> int:
        result = max(itertools.accumulate([0] + gain))

        return result


result = Solution().largestAltitude(gain=[-5, 1, 5, 0, -7])
print(result)
