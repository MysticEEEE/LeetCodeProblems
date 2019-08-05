class Solution(object):
    def findUnsortedSubarray(self, nums):
        sorted_nums = sorted(nums)
        if nums == sorted_nums:
            return 0
        while nums[-1] == max(nums):
            nums.pop()
        while nums[0] == min(nums):
            nums.pop(0)
        return len(nums)

    def findUnsortedSubarray3(self,nums):
        low = 0
        high = len(nums)-1
        sorted_nums = sorted(nums)
        while low <= high and nums[low] == sorted_nums[low]:
            low += 1
        while low <= high and nums[high] == sorted_nums[high]:
            high -=1
        return high - low + 1


    def findUnsortedSubarray1(self, nums):
        diff = [i for i, (a, b) in enumerate(zip(nums, sorted(nums))) if a != b]
        return len(diff) and max(diff) - min(diff) + 1





if __name__ == "__main__":
    list = [1,2,3,4,5]
    a = Solution()
    print(a.findUnsortedSubarray3(list))
    print(a.findUnsortedSubarray(list))
    print(a.findUnsortedSubarray1(list))
    