class Solution(object):
    def moveZeroes(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        for i in nums:
            if i ==0:
                #print(i)
                nums.remove(i)
                nums.append(0)
        return nums

    ##双指针
    def moveZeroes2(self, nums):
        slow  = 0
        for fast in range(len(nums)):
            if nums[fast] != 0:
                tmp = nums[slow]
                nums[slow] = nums[fast]
                nums[fast] = tmp
                slow += 1
        return nums

if __name__ == "__main__":
    s = Solution()
    m = [0,1,0,3,12]
    print(s.moveZeroes2(m))