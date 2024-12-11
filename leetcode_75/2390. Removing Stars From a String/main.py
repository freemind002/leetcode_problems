class Solution:
    def removeStars(self, s: str) -> str:
        stack = []

        for s_str in s:
            stack.pop() if s_str == "*" else stack.append(s_str)

        return "".join(stack)


result = Solution().removeStars(s="erase*****")
print(result)
