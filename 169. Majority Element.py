class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        d = {}
        count = len(nums) /2
        for i in nums:
            if i not in d:
                d[i] =1
            else:
                d[i] += 1
        for c in d:
            if d[c] > count:
                return c

    def majorityElement2(self, nums):
        import collections
        counts = collections.Counter(nums)
        return max(counts.keys(), key=counts.get)

    def majorityElement3(self, nums):
        nums.sort()
        return nums[len(nums)//2]

