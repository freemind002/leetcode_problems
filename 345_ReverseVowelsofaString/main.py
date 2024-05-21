class Solution:
    def reverseVowels(self, s: str) -> str:
        tmp_dic = {
            "a": "a",
            "e": "e",
            "i": "i",
            "o": "o",
            "u": "u",
            "A": "A",
            "E": "E",
            "I": "I",
            "O": "O",
            "U": "U",
        }
        key_list = [index for index, value in enumerate(s) if tmp_dic.get(value)]
        value_list = [value for index, value in enumerate(s) if tmp_dic.get(value)][::-1]
        new_dic = {key: value for key, value in zip(key_list, value_list)}
        result = "".join(
            [
                new_dic[index] if new_dic.get(index) else item
                for index, item in enumerate(s)
            ]
        )

        return result


result = Solution().reverseVowels("leetcode")
print(result)
