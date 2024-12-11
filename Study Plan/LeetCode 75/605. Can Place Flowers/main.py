from typing import List


class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        flowerbed_len = len(flowerbed)
        for n_no in range(n):
            for index, flower in enumerate(flowerbed):
                if (
                    flower == 0
                    and (index == 0 or flowerbed[index - 1] == 0)
                    and (index == flowerbed_len - 1 or flowerbed[index + 1] == 0)
                ):
                    flowerbed[index] = 1
                    n -= 1
                    break

        return True if n==0 else False


result = Solution().canPlaceFlowers([0], 1)
print(result)
