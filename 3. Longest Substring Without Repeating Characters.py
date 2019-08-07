class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        tmp =[]
        maxLength = 0
        for i in s :
            if i not in tmp:
                tmp.append(i)
                maxLength = max(maxLength,len(tmp))
            else:
                del tmp[0:tmp.index(i)+1]
                tmp.append(i)
        return maxLength

    
    def lengthOfLongestSubstringHash(self,s):
        dict1 = {}
        maxLength = 0
        duplicIndex = -1
        for i,c in enumerate(s):
            if c in dict1 and dict1[c] > duplicIndex:
                duplicIndex = dict1[c]
                dict1[c] = i
            else:
                dict1[c] = i
            maxLength = max(i - duplicIndex, maxLength)
        return maxLength

if __name__ == "__main__":
    a = Solution()
    s = "ddpvpfb"
    m = a.lengthOfLongestSubstring(s)
    h = a.lengthOfLongestSubstringHash(s)
    print(m)
    print(h)
