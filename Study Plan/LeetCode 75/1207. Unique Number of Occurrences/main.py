from collections import Counter
from typing import List


class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        count_dic = Counter(arr)
        count_set = set(count_dic.values())

        return len(count_set) == len(count_dic)


result = Solution().uniqueOccurrences(arr=[3, 5, -2, -3, -6, -6])
print(result)
