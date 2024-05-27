from typing import List


class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        left = 0
        for right, num in enumerate(nums):
            if num != 0:
                nums[right], nums[left] = nums[left], nums[right]
                left += 1
        print(nums)


Solution().moveZeroes([0, 1, 0, 3, 12])
