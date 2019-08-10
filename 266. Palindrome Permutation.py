class Solution(object):
    def canPermutePalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        import collections
        count = 0
        dict1 = dict(collections.Counter(s))
        for i in dict1.values():
            if i % 2 ==0:
                continue
            else:
                count += 1
        if count <= 1:
            return True
        else:
            return False
if __name__ == "__main__":
    s = "abbacb"
    # count = 0
    # import collections
    # dict1 = dict(collections.Counter(s))
    # for i in dict1.values():
    #     if i % 2 ==0:
    #         continue
    #     else:
    #         count += 1
    # if count <= 1:
    #     print(True)
    # else:
    #     print(False)
    solution = Solution()
            

    
    print(solution.canPermutePalindrome(s))