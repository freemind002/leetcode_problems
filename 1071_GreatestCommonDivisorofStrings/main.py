from math import gcd


class Solution:
    def gcdOfStrings(self, str1: str, str2: str) -> str:
        result = "" if str1 + str2 != str2 + str1 else str1[: gcd(len(str1), len(str2))]

        return result


result = Solution().gcdOfStrings("ABABAB", "ABAB")
print(result)
