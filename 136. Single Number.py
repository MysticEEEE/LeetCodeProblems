class Solution(object):
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        d = {}
        for i in nums:
            if i not in d:
                d[i] = 1
            else:
                d[i] += 1
        for i in d:
            if d[i] <=1:
                return i
            # else:
            #     return None
if __name__ == "__main__":
    s = Solution()
    m = [4,1,2,1,2]
    d = {}
    for i in m:
        if i not in d:
            d[i] = 1
        else:
            d[i] += 1
    # for i in d:
    #     if d[i] <=1:
    #         return i
    #     else:
    #         return None
    print(len(d))