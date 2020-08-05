# Valid Palindrome
class Solution:
    """
    @param s: A string
    @return: Whether the string is a valid palindrome
    """
    def isPalindrome(self, s):
        start, end = 0, len(s) - 1
        while start < end:
            while start < end and not s[start].isalnum():
                start += 1
            while start < end and not s[end].isalnum():
                end -= 1
            if start < end and s[start].lower() != s[end].lower():
                return False
            start += 1
            end -= 1
        return True


# Valid PalindromeII
class Solution2:
    """
    @param s: a string
    @return bool: whether you can make s a palindrome by deleting at most one character
    """
    def validPalindrome(self, s):
        # Write your code here
        start, end = 0, len(s) - 1
        
        while start < end:
            if s[start] != s[end]:
                return self.isSubPalindrome(start+1, end, s) or self.isSubPalindrome(start, end-1, s)
            start += 1
            end -= 1
        return True
    
    def isSubPalindrome(self, start, end, s):
        while start < end:
            if s[start] != s[end]:
                return False
            start += 1
            end -= 1
        return True
