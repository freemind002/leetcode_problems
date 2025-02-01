class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
        result = chr(sum(ord(y) for y in t) - sum(ord(x) for x in s))

        return result


result = Solution().findTheDifference(s="abcd", t="abcde")
print(result)
