class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x < 0:
            return False
        x_str = str(x)
        x_reverse = x_str[::-1]

        return True if x_str == x_reverse else False
    
result = Solution().isPalindrome(121)
print(result)
