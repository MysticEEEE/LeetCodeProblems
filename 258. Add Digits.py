class Solution(object):
    def addDigits(self, num):
        """
        :type num: int
        :rtype: int
        """
        
        while num >9:
            num = sum(int(i) for i in str(num))
        return num

        return self.addDigits(sum(int(i) for i in str(num)) if num

if __name__ == "__main__":
    a = Solution