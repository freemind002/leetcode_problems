from itertools import zip_longest


class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        result = "".join(
            [word for pair in zip_longest(word1, word2, fillvalue="") for word in pair]
        )

        return result


result = Solution().mergeAlternately("abc", "pqr")
print(result)
