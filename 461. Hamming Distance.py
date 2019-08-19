class Solution(object):
    def hammingDistance(self, x, y):
        """
        :type x: int
        :type y: int
        :rtype: int
        """
        s = bin(x^y)
        return s.count('1')
        #return bin(x^y).count('1')
        #return format(x^y,'b').count('1')

if __name__ == "__main__":
    s = Solution()
    ham = s.hammingDistance(1,4)
    print(ham)
    print(bin(1^4))