class Solution(object):
    def isHappy(self, n):
        """
        :type n: int
        :rtype: bool
        """
        lst = []
        nums = set()
        while n != 1:
            tmp = sum([int(i)**2 for i in str(n)])
            # for i in str(n):
            #     lst.append(int(i)**2)
            # tmp = sum(lst)
            n = tmp
            if n not in nums:
                nums.add(n)
            else:
                return False
        return True



n = 123
list1 = []
lst = []
tmp = sum([int(i)**2 for i in str(n)])
tmp1 = [int(i)**2 for i in str(n)]

for i in str(n):
    lst.append(int(i)**2)

print(lst)