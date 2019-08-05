class Solution(object):
    def jump(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        steps = 1
        lastIndex = len(nums)-1
        curValue = nums[0]
        maxJump = 0
        if nums[0] == 0 or len(nums) < 2 :
                return 0
        # while curPos <= maxJump:
        for curPos in range(lastIndex):
            maxJump = max(maxJump, curPos+ nums[curPos])
            if curPos == curValue:
                curValue = maxJump
                steps += 1
        return steps

        # while maxJump < lastIndex:
        #     steps += 1
        #     maxJump = max(maxJump, curPos+ nums[curPos])
        #     curPos = maxJump
        # return steps

    def jump2(self, nums):
        res = 0
        a = 0
        b = 0
        for e in nums[:-1]:
            if e > b:
                b = e
            if a == 0:
                a = b
                res += 1
            a -= 1
            b -= 1
        return res

if __name__ == "__main__":
    a= Solution()
    m = [1,2]
    print(a.jump(m))