class Solution:
    """
    @param s: A string
    @return: Whether the string is a valid palindrome
    """
    def isPalindrome(self, s):
        # write your code here
        s = ''.join([ch for ch in s.lower() if ch.isalnum()])
        
        left, right = 0, len(s) - 1
        
        while left < right:
            if s[left] == s[right]:
                left += 1
                right -=1
            else:
                return False
        return True