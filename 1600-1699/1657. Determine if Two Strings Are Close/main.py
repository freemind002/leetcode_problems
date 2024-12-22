from collections import Counter


class Solution:
    def closeStrings(self, word1: str, word2: str) -> bool:
        return (
            Counter(Counter(word1).values()) == Counter(Counter(word2).values())
            and Counter(word1).keys() == Counter(word2).keys()
        )


result = Solution().closeStrings(word1="abc", word2="bca")
print(result)
