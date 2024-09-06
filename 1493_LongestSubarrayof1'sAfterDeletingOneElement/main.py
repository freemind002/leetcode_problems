from typing import List


class Solution:
    def longestSubarray(self, nums: List[int]) -> int:
        left = 0
        result = 0
        zero_count = 0

        for right, num in enumerate(nums):
            if num == 0:
                zero_count += 1

            while zero_count > 1:
                if nums[left] == 0:
                    zero_count -= 1
                left += 1

            result = max(result, right - left)

        return result


result = Solution().longestSubarray(nums=[1, 1, 0, 1])
print(result)
