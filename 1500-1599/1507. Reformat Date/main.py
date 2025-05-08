import calendar
import re
from datetime import datetime


class Solution:
    def reformatDate(self, date: str) -> str:
        # 建立月份縮寫對應dict
        month_dict = {
            calendar.month_abbr[month]: f"{month:02}" for month in range(1, 13)
        }

        # 使用正則獲取日期元件
        match = re.match(r"(\d{1,2})(?:st|nd|rd|th) (\w{3}) (\d{4})", date)
        if match:
            day, month_abbr, year = match.groups()
            if month_dict.get(month_abbr):
                result = "{}-{}-{}".format(year, month_dict[month_abbr], day.zfill(2))
                try:
                    datetime.strptime(result, "%Y-%m-%d")
                except ValueError:
                    raise ValueError(f"無效的日期：{result}")
                else:
                    return result
            else:
                raise ValueError(f"未知的月份縮寫：{month_abbr}")
        else:
            raise ValueError(f"日期格式有錯誤：{date}")


result = Solution().reformatDate("20th Oct 2052")
print(result)
