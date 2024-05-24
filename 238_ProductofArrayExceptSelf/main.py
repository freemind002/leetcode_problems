"""需要再學習為什麼"""

# [24, 12, 8, 6]
from typing import List


class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        # 初始化前綴積和後綴積的陣列
        prefix_products = [1 for num in nums]
        suffix_products = [1 for num in nums]

        # 計算前綴積
        for index, num in enumerate(nums[:-1], 1):
            prefix_products[index] = prefix_products[index - 1] * num

        # 計算後綴積
        for index, num in reversed(list(enumerate(nums[1:]))):
            suffix_products[index] = suffix_products[index + 1] * num

        # 計算結果
        answer = [
            prefix * suffix for prefix, suffix in zip(prefix_products, suffix_products)
        ]

        return answer


answer = Solution().productExceptSelf([1, 2, 3, 4])
print(answer)
