class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        i = 0
        s_len = len(s)
        for t_value in t:
            if i < s_len and s[i] == t_value:
                i += 1

        return i == s_len


result = Solution().isSubsequence("acb", "ahbgdc")
print(result)
