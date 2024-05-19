from typing import List


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        result = [
            [index_01, index_02]
            for index_01, num_01 in enumerate(nums[:-1])
            for index_02, num_02 in enumerate(nums[index_01 + 1 :], index_01 + 1)
            if num_01 + num_02 == target
        ]
        return result[0] if result else []


result = Solution().twoSum(nums=[3, 2, 4], target=6)
print(result)
