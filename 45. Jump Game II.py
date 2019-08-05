class Solution(object):
    def jump(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        steps = 0
        curPos = 0
        lastIndex = len(nums)-1
        maxJump = 0
        # while curPos <= maxJump:
        while maxJump <= lastIndex:
            steps += 1
            maxJump = max(maxJump, curPos+ nums[curPos])
            curPos = maxJump
        return steps

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
    m = [2,3,1,1,4]
    print(a.jump(m))