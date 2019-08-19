class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        profit = 0
        Min = float('inf')
        for i in prices:
            Min = min(Min,i)
            profit = max(profit,i-Min)
        return profit 

    def maxProfitBrute(self, prices):
        l = prices
        profit = 0
        for i in range(len(l)):
            for j in range(i,len(l)):
                profit = max(profit,prices[j]-prices[i])
        return profit

if __name__ == "__main__":
    m = [1,2,3,7,2,5,7,1,2]
    s = Solution()
    print(s.maxProfit(m))