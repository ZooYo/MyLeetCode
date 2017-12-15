'''
Created on 2017年2月23日

@author: Luke
'''
'''
nums1 = [1, 3]
nums2 = [2]
The median is 2.0
nums1 = [1, 2]
nums2 = [3, 4]
The median is (2 + 3)/2 = 2.5
'''
'''
class Solution(object): #合併後排序，再求中位數
    def findMedianSortedArrays(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        """
        nums3=nums1+nums2
        nums3.sort()
        mid=len(nums3)//2
        print (nums3)
        if len(nums3)%2==0:       
            return (nums3[mid-1]+nums3[mid])/2
        else:
            return nums3[mid]
'''
class Solution(object):
    def findMedianSortedArrays(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        """
        nums1.extend(nums2)
        print(nums1)
        a=sorted(nums1)
        print(a)
        if len(a)%2==0 :
            r=(a[len(a)//2-1]+a[len(a)//2])/2.0
        else:
            r=a[len(a)/2]
        return r
example=Solution()
print(example.findMedianSortedArrays([1, 3],[2, 4]))