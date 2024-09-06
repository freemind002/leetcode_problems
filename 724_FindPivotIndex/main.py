from typing import List


class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        total = sum(nums)
        left_total = 0

        for index, num in enumerate(nums):
            if left_total == total - left_total - num:
                return index
            left_total += num

        return -1


result = Solution().pivotIndex(nums=[1, 7, 3, 6, 5, 6])
print(result)
