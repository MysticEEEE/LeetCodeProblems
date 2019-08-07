class Solution(object):
    def twoSum(self, nums,target):
        res = []
        indexLength = len(nums)
        for i in range(indexLength) :
            r = target - nums[i]
            # print(r)
            if r in nums and nums.index(r) != i:
                res.append(i)
                res.append(nums.index(r))
                # return True
                return res

    def twoSumHash(self, nums,target):
        dict1 = {}
        for i, m in enumerate(nums):
            if dict1.get(target - m) is not None:
                return [i,dict1.get(target - m)]
            dict1[m] = i
    ###############################################
    def twoSum2(self, nums,target):
        for i in range(len(nums)):
            if(target-nums[i] in nums and i != nums.index(target-nums[i])):
                    return [i,nums.index(target-nums[i])]
    ###############################################
    def twoSum3(self, nums,target):
        for i in range(len(nums)-1):
            m = nums[i]
            j = i+1
            while j < len(nums):
                if target == (m + nums[j]):
                    return [i,j]
                else:
                    j += 1
    ##############################################
    def twoSum4(self,nums,target):
        size = len(nums)
        for i, m in enumerate(nums):
            j = i + 1
            while j < size:
                print(j)
                if target == (m + nums[j]):
                    return [i, j]
                else:
                    # print(i, j, m + _n, " didn't match!")
                    j += 1

if __name__ == "__main__":
    a = Solution()
    list1 = [3,3]
    target = 6
    # print(list1.index(3,-len(list1)-1))
    # print(a.twoSum2(list1,target))
    print(a.twoSum(list1,target))
    print(a.twoSumHash(list1,target))
    # print(a.twoSum4(list1,target))
    


