class Solution:
    def maxVowels(self, s: str, k: int) -> int:
        vowel_dic = {"a": "a", "e": "e", "i": "i", "o": "o", "u": "u"}
        curr_count = sum([1 if vowel_dic.get(s_value) else 0 for s_value in s[:k]])
        max_count = curr_count

        for index, s_value in enumerate(s[k:], k):
            # 符合條件，所以+=1
            if vowel_dic.get(s_value):
                curr_count += 1
            # 符合條件，但已經被移出窗口範圍，因此-=1
            if vowel_dic.get(s[index - k]):
                curr_count -= 1
            max_count = max(max_count, curr_count)

        return max_count


result = Solution().maxVowels(s="leetcode", k=3)
print(result)
