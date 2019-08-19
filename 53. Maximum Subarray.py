class Solution(object):
    def maxSubArrayBrute(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        maxsum = -float('inf')
        slow = 0
        while slow < len(nums):
            for fast in range(slow,len(nums)):
                tmp = sum(nums[slow:fast+1])
                maxsum = max(maxsum,sum(nums[slow:fast+1]))
                #print(slow,fast,tmp)
            slow += 1
        return maxsum
    
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
         """
        for i in range(1, len(nums)):
            nums[i]= nums[i] + max(nums[i-1], 0)
        return max(nums)

if __name__ == "__main__":
    s = Solution()
    m = [ x for x in range(-5000,20000)]
    n = [-2,-1]
    #print(s.maxSubArrayBrute(m))
    print(s.maxSubArray(m))