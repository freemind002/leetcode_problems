class Solution:
    def romanToInt(self, s: str) -> int:
        tmp_dic = {"I": 1, "V": 5, "X": 10, "L": 50, "C": 100, "D": 500, "M": 1000}

        s_len = len(s)
        ans = sum(
            (
                -tmp_dic[key]
                if (index < s_len and tmp_dic[key] < tmp_dic[s[index]])
                else tmp_dic[key]
                for index, key in enumerate(s, 1)
            )
        )

        return ans


ans = Solution().romanToInt("MCMXCIV")
print(ans)
