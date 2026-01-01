from typing import List


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # 哈希表用來存儲已經遍歷過的數值及其索引
        seen = {}

        # 遍歷 nums
        for index, num in enumerate(nums):
            complement = target - num  # 計算差值

            if seen.get(complement) is not None:  # 如果差值已經在哈希表中，說明找到結果
                return [seen[complement], index]

            # 如果沒有找到，紀錄當前數值及其索引
            seen[num] = index

        return []  # 如果沒有結果，返回空列表


result = Solution().twoSum(nums=[3, 2, 4], target=6)
print(result)
