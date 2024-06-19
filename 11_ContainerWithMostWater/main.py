from typing import List


class Solution:
    def maxArea(self, height: List[int]) -> int:
        maxvol = 0
        left = 0
        right = len(height) - 1

        while True:
            if height[left] <= height[right]:
                maxvol = max(height[left] * (right - left), maxvol)
                left += 1
            else:
                maxvol = max(height[right] * (right - left), maxvol)
                right -= 1
            if right == left:
                break

        return maxvol


result = Solution().maxArea([1, 8, 6, 2, 5, 4, 8, 3, 7])
print(result)
