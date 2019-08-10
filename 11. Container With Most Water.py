class Solution(object):
    def maxAreaBrute(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        l = height
        size = 0
        for i in range(len(l)):
            for j in range(i,len(l)):
                print(l[i],l[j])
                if l[i] < l[j]:
                    size = max(size,l[i] * (j-i))
                else:
                    size = max(size,l[j] * (j-i))
        return size           

        ##双指针
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        head = 0
        tail = len(height)-1
        size = 0
        while head < tail:
            size = max(size,min(height[head],height[tail]) * (tail-head))
            if height[head] < height[tail]:
                head += 1
            else:
                tail -= 1
        return size


# l = [1,8,6,2,5,4,8,3,7]
# d = {}
# for i,s in enumerate(l):
#     j = i+1
#     d.update({j:s})

# print(d.values())
if __name__ == "__main__":
    solution = Solution()
    l = [1,8,6,2,5,4,8,3,7]
    print(solution.maxArea(l))