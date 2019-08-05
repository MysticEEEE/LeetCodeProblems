class Solution(object):
    def sumOfDigits(self, A):
        """
        :type A: List[int]
        :rtype: int
        """
        
        minValue = min(A)
        m = sum(int(i) for i in str(minValue))
        if m %2 ==0:
            return 1
        else:
            return 0

if __name__ == "__main__":
    a = Solution()
    m = [34,23,1,24,75,33,54,8]
    n = a.sumOfDigits(m)

    print(n)