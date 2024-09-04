from typing import List


class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        curr_sum = max_sum = sum(nums[:k])
        for index in range(k, len(nums)):
            curr_sum += nums[index] - nums[index - k]
            max_sum = max(max_sum, curr_sum)

        return max_sum / k


result = Solution().findMaxAverage(nums=[1, 12, -5, -6, 50, 3], k=4)
print(result)
