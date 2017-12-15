'''
Created on 2017年3月11日

@author: Luke
'''
'''
運用threeSum的方法
在判斷和在目標的左右邊，利用變數p來判斷
回傳時再以Target為中心利用p決定+distance或-distance
'''
class Solution(object):
    def threeSumClosest(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        nums.sort()
        distance=abs(target-(nums[0]+nums[1]+nums[2]))
        p=""
        for i in range(len(nums)-2):
            if i>0 and nums[i]==nums[i-1]:
                continue
            l=i+1
            r=len(nums)-1
            while l<r:
                s=nums[i]+nums[l]+nums[r]
                if s>target:
                    if abs(s-target)<=distance:
                        p="l" if s>target else "r"
                        distance=abs(s-target)
                    r-=1
                elif s<target:
                    if abs(s-target)<=distance:
                        p="l" if s>target else "r"
                        distance=abs(s-target)
                    l+=1
                else:
                    return s
        if p=="r":
            return target-distance
        else:
            return target+distance


example=Solution()
print(example.threeSumClosest([1,1,-1],2))