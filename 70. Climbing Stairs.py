class Solution(object):
    def climbStairs(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n ==1:
            return 1
        dp = [None]*(n+1)
        dp[1] = 1
        dp[2] =2
        for i in range(3,n+1):
            dp[i] = dp[i-1]+dp[i-2]
        return dp[n]
if __name__ == "__main__":
    s =  Solution()
    print(s.climbStairs(6))