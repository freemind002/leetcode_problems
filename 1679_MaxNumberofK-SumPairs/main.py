from typing import List


class Solution:
    def maxOperations(self, nums: List[int], k: int) -> int:
        nums.sort()

        left = 0
        right = len(nums) - 1
        operation = 0

        while left < right:
            print(left, right)
            if (nums[left] + nums[right]) == k:
                operation += 1
                left += 1
                right -= 1
            elif (nums[left] + nums[right]) < k:
                left += 1
            else:
                right -= 1
            print(left, right)

        return operation


result = Solution().maxOperations(nums=[3, 1, 3, 4, 3], k=6)
print(result)
