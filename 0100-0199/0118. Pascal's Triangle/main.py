from typing import List


class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        result = []  # 用來儲存整個 Pascal's Triangle，每一列是一個 list

        for i in range(numRows):
            if i == 0:
                result.append([1])
            else:
                prev = result[-1]  # 取出上一列，準備用來生成當前列
                row = [1]  # 每一個row的開頭為1
                # 每個中間的元素 = 前一列中相鄰的兩個元素相加
                middle = [prev[j - 1] + prev[j] for j in range(1, i)]
                # 新的一列 = [1]（開頭）+ 中間元素 + [1]（結尾）
                row += middle
                row += [1]
                result.append(row)

        return result


result = Solution().generate(3)
print(result)
