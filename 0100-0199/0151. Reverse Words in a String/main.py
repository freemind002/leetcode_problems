class Solution:
    def reverseWords(self, s: str) -> str:
        result = " ".join(s.split()[::-1])

        return result


result = Solution().reverseWords("  hello world  ")
print(result)
