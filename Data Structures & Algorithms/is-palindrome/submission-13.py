class Solution:
    def isPalindrome(self, s: str) -> bool:
        concat = ''.join([c.lower() for c in s if c.isalnum()])
        l = 0
        r = len(concat)-1
        while l < r:
            if concat[l] != concat[r]:
                return False
            l += 1
            r -= 1
        return True
