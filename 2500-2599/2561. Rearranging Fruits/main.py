from collections import Counter
from typing import List


class Solution:
    def minCost(self, basket1: List[int], basket2: List[int]) -> int:
        freq1 = Counter(basket1)
        freq2 = Counter(basket2)
        total = Counter(basket1 + basket2)

        # Step 1: 如果有水果出現奇數次，無解
        for fruit, count in total.items():
            if count % 2 != 0:
                return -1

        # Step 2: 計算每種水果，在哪個籃子多出來
        extra1, extra2 = [], []
        for fruit in total.keys():
            diff = freq1[fruit] - total[fruit] // 2
            if diff > 0:
                extra1 += [fruit] * diff
            elif diff < 0:
                extra2 += [fruit] * (-diff)

        # Step 3: 把多出來的水果排序，準備配對
        # 這樣配對的效果是：
        # 小的對大的換(i 小、j 大)
        # 這樣 min(i, j) 就是 i，保證交換成本盡可能低。
        # 如果 i > 2 * min_fruit，那麼間接交換成本（2 * min_fruit）會更划算。
        extra1.sort()
        extra2.sort(reverse=True)

        min_fruit_02 = min(total.keys()) * 2  # 全場最小的水果編號
        cost = sum(min(i, j, min_fruit_02) for i, j in zip(extra1, extra2))
        # min_fruit = min(total.keys())  # 全場最小的水果編號
        # cost=0
        # for i, j in zip(extra1, extra2):
        #     direct_swap = min(i, j)
        #     double_swap = 2 * min_fruit
        #     cost += min(direct_swap, double_swap)

        return cost


result = Solution().minCost(basket1=[4, 2, 2, 2], basket2=[1, 4, 1, 2])
print(result)
