class Solution(object):
    def canJump(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        curPos = len(nums)-1
        curValue= 0
        for i in range(curPos,-1,-1):
            if i + nums[i] >= curPos:
                curPos = i
                print(curPos)
        return curPos == 0


    
    def canJump2(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        
        last_Index = len(nums)-1
        #initialize max jump distance 
        maxJump = 0
        curPos = 0
        while curPos <= maxJump:
            maxJump = max(maxJump, curPos+ nums[curPos])
            curPos += 1
            if maxJump >= last_Index:
                return True
        return False

if __name__ == "__main__":
    a= Solution()
    m = [1, 4, 2, 1, 0, 2, 0]
    print(a.canJump(m))
