class Solution(object):
    def findMedianSortedArraysWithBinarySearch(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        使用割的方法，比较割后的左右部分，目的是寻找L1Max < R2Min, L2Max < L1Min 
        那么需要找到的数就是left = max(L1Max,L2max), right = min(R1Min,R2min)
        median = (left +right) /2
        使用二分查找法来取得“割”的位置
        """
        ###
        m = len(nums1)
        n = len(nums2)
        if m > n:
            return self.findMedianSortedArraysWithBinarySearch(nums2, nums1)

        lo = 0
        hi = 2 * m
        while lo <= hi:
            # print(hi)
            c1 = (lo+hi) // 2
            # print(c1)
            c2 = m + n - c1
            if c1 == 0:
                L1Max = float("-inf")
            else:
                L1Max = nums1[(c1-1)//2]
            if c1 == 2*m:
                R1min = float("inf")
            else:
                R1min = nums1[c1//2]
            if c2 == 0:
                L2Max = float("-inf")
            else:
                L2Max = nums2[(c2-1)//2]
            if c2 == 2*n:
                R2min = float("inf")
            else:
                R2min = nums2[c2//2]
            if L1Max > R2min:
                hi = c1 - 1
            elif L2Max > R1min:
                lo = c1 + 1
            else:
                return (max(L1Max, L2Max)+min(R1min, R2min)) / 2.0

    def findMedianSortedArraysWithKthSmallestEle(self, nums1, nums2):
        """ 
        使用找第k个最小数字的思想 

        """
        m = len(nums1)
        n = len(nums2)
        odd = (m+n+1) // 2
        even = (m+n+2) // 2
        return (self.kthSmallestEle(nums1, 0, m-1, nums2, 0, n-1, odd)+self.kthSmallestEle(nums1, 0, m-1, nums2, 0, n-1, even))/2.0

    def kthSmallestEle(self, nums1: list, start1, end1, nums2: list, start2, end2, k):
        # 两个数组的长度
        len1 = end1 - start1 + 1
        len2 = end2 - start2 + 1
        # 保持len1一直比len2短，方便计算
        if len1 > len2:
            return self.kthSmallestEle(nums2, start2, end2, nums1, start1, end1, k)
        # 如果短的数组空了，则所求的值在长数组的第k+start2-1的位置
        if len1 == 0:
            return nums2[k + start2 - 1]
        # 如果k=1，则比较两个数组的第一个元素，小的那个就是所找的值
        if k == 1:
            return min(nums1[start1], nums2[start2])
        # 指针i，j选取元素，判断条件是len1，len2是否比 k//2小
        i = start1 + min(len1, k//2) - 1
        j = start2 + min(len2, k//2) - 1
        # 通过判断指针指向的两个元素大小，来判断移除哪一个数组的元素
        if nums1[i] > nums2[j]:
            # return True
            return self.kthSmallestEle(nums1, start1, end1, nums2, j+1, end2, (k-(j-start2+1)))
        else:
            # return False
            return self.kthSmallestEle(nums1, i+1, end1, nums2, start2, end2, (k-(i-start1+1)))

    def findMedianSortedArraysWithAppend(self, nums1, nums2):
        m = len(nums1)
        n = len(nums2)
        nums3 = nums1 + nums2
        res = sorted(nums3)
        l = len(nums3)
        # print(res)
        # print(l)
        if l % 2 == 0:
            return (res[l//2]+res[(l//2)-1])/2.0
        else:
            return (res[l//2])


if __name__ == "__main__":
    l1 = [1, 3, 10, 15]
    l2 = [2, 6, 7, 8, 11]
    a = Solution()
    # print(a.findMedianSortedArraysWithBinarySearch(l1,l2))
    # print(a.findMedianSortedArraysWithAppend(l1,l2))
    # l1.extend(l2)
    # print(l1)
    print(a.kthSmallestEle(l1, 0, 3, l2, 0, 4, 3))
