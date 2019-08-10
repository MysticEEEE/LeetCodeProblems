class Solution(object):
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        nums.sort()
        lst = []
        head = 0 
        for head in range(len(nums)-2):
            if nums[head] > 0:
                break
            if head > 0 and nums[head] == nums[head-1]:
                continue
            target = head + 1
            tail = len(nums)-1
            while target < tail:
                sum = nums[head]+nums[target]+nums[tail]
                if sum > 0:
                    tail -= 1
                elif sum < 0:
                    target += 1
                else:
                    # print(sum)
                    lst.append([nums[head],nums[target],nums[tail]])
                    target += 1
                    tail -= 1 
                    while target < tail and nums[tail] == nums[tail+1]:
                        tail -= 1
                    while target < tail and nums[target] == nums[target-1]:
                        target += 1
        return lst 
    
    
    # def threeSumDict(self, nums):
    #     dic = {}
    #     res = []
    #     for i in nums:
    #         if i in dic:
    #             dic[i] += 1
    #         else:
    #             dic[i] = 1
    #     pos =[i for i in dic if i > 0]
    #     neg =[i for i in dic if i < 0]
    #     neg.sort()
    #     if 0 in dic and dic[0] >= 3:
    #         res.append([0,0,0])
    #     for i in pos:
    #         for j in neg:
    #             k = -i-j
    #             if k in dic:
    #                 if (k==i or k==j) and dic[k] >= 2:
    #                     res.append([i,k,j])
    #                 elif i>k>j:
    #                     res.append([i,k,j])
    #                 if k < j:
    #                     break
    #     return res 

    def threeSumDict(self, nums):
        lst = []
        dic = {}
        for i in nums:
            if i in dic:
                dic[i] += 1
            else:
                dic[i] =  1
        if 0 in dic and dic[0] >2:
            lst.append([0,0,0])
        pos = [i for i in dic if i > 0]
        neg = [i for i in dic if i < 0]
        for p in pos:
            for n in neg:
                target = 0-(p+n)
                if target in dic:
                    if (target == p or target ==n) and dic[target]>=2:
                        lst.append([n,target,p])
                    elif p > target > n:
                        lst.append([n,target,p])
        return lst
if __name__ == "__main__":
    s = Solution()
    l = [-1, 0, 1, 2, -1, -4]
    print(s.threeSumDict(l))
# l_index = []
# for i in range(len(l)):
#     l_index.append(i)
# print(l_index)
# d = dict(zip(l,l_index))
# dic = {}
# for i in l:
#     if i in dic:
#         dic[i] += 1
#     else:
#         dic[i] = 1
# print(d) 
# print(dic)
# pos = [i for i in d if i>0]
# neg = [i for i in d if i<0]
# print(pos,neg)
# neg.sort()
# if d[i]>2:
#     list

