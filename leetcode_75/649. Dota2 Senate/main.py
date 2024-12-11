from collections import deque


class Solution:
    def predictPartyVictory(self, senate: str) -> str:
        # 用 deque 分別記錄「R」（Radiant）和「D」（Dire）議員的索引。
        q_r = deque(index for index, item in enumerate(senate) if item == "R")
        q_d = deque(index for index, item in enumerate(senate) if item == "D")
        # nums 為參議院總人數。
        nums = len(senate)

        # 模擬投票
        # 合併索引比較與重新排隊邏輯
        while q_r and q_d:
            r, d = q_r.popleft(), q_d.popleft()
            (q_r if r < d else q_d).append((r if r < d else d) + nums)

        return "Radiant" if q_r else "Dire"


result = Solution().predictPartyVictory(senate="RDD")
print(result)
