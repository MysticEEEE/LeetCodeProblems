class Solution(object):
    def findDisappearedNumbersBrute(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        if len(nums) == 0:
            return None
        nums.sort()
        n = set(nums)
        print(n)
        m = [ x for x in range(1,len(nums)+1)]
        l = [ x for x in m if x not in n]
        return l

    def findDisappearedNumbers2(self, nums):
        for n in nums:
            index = abs(n) - 1
            print(nums)
            print(index,nums[index],-abs(nums[index]))
            nums[index] = -abs(nums[index])
        return [i + 1 for i, n in enumerate(nums) if n > 0]

    def findDisappearedNumbers3(self, nums):
        m = set(nums)
        l = [x for x in range(1,len(nums)+1)]
        n = set(l)
        #res = list(n-m)
        res = list(n.difference(m))
        return res
        



if __name__ == "__main__":
    s = Solution()
    m = [4,3,2,7,2,2,3,1]
    n = [1,2,3,4,5,6,7,8]
    l = set(n)
    print(s.findDisappearedNumbers3(m))