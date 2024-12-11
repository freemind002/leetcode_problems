from itertools import chain, groupby
from typing import List


class Solution:
    def compress(self, chars: List[str]) -> int:
        chars[:] = list(
            chain.from_iterable(
                [char] + list(str(count)) if (count := len(list(group))) > 1 else [char]
                for char, group in groupby(chars)
            )
        )

        return len(chars)


result = Solution().compress(["a", "a", "a", "b", "b", "a", "a"])
print(result)
