class Solution:
    """
    @param s: the maximum length of s is 1000
    @return: the longest palindromic subsequence's length
    """
    def longestPalindromeSubseq(self, s):
        # write your code here
        len_s=len(s)
        if len_s<=1:
            return len_s
            
        dp=[[0 for _ in range(len_s)] for _ in range(len_s)]
        
        for i in range(len_s):
            for j in range(len_s-i):
                if j==j+i:
                    dp[j][j+i]=1
                else:
                    dp[j][j+i]=max((2+dp[j+1][j+i-1] if s[j]==s[j+i] else 0),
                                  dp[j][j+i-1],
                                  dp[j+1][j+i])
        return dp[0][len_s-1]