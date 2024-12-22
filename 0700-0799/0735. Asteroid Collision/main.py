from typing import List


class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        # 用來儲存當前存活的小行星
        stack = []  # 用来存储当前存活的小行星

        for asteroid in asteroids:
            # 如果小行星向右移動，append到stack
            if asteroid > 0:
                stack.append(asteroid)
            else:
                # 當前小行星向左移動，需處理可能的碰撞
                while stack and stack[-1] > 0:
                    # stack的小行星向右，小行星碰撞
                    if stack[-1] + asteroid == 0:
                        # 若兩個小行星質量相同，兩個都消失
                        stack.pop()
                        break
                    elif stack[-1] + asteroid < 0:
                        # 當前小行星質量更大，stack的小行星消失
                        stack.pop()
                        continue
                    else:
                        # 當前小行星質量更小，當前小行星消失
                        break
                else:
                    # 若stack為空或stack小行星向左，stack append 當前小行星
                    stack.append(asteroid)

        return stack


result = Solution().asteroidCollision(asteroids=[5, 10, -5])
print(result)
