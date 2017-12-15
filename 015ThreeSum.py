'''
Created on 2017年3月8日

@author: Luke
'''
'''
class Solution(object):
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        nlist =[]
        nums=sorted(nums)
        for i in range(len(nums)):
            for j in range(i+1,len(nums)):
                for k in range(j+1,len(nums)):
                    if(nums[i]+nums[j]+nums[k])==0 and [nums[i],nums[j],nums[k]] not in nlist:
                        nlist.append([nums[i],nums[j],nums[k]])
        return nlist
'''
'''
先排序
運用l,r為左右邊界
和若是比0小則左邊界往右，比0大右邊界往左
找到合為0後讓左右邊界都跳過同樣的數字在往中間找
'''
class Solution(object):
    def threeSum(self, nums):
        res = []
        nums.sort()
        #print(nums)
        for i in range(len(nums)-2):
            if i > 0 and nums[i] == nums[i-1]:
                continue
            l, r = i+1, len(nums)-1
            while l < r:
                print("i=%d,l=%d,r=%d"%(i,l,r))
                print("nums[%d]=%d,nums[%d]=%d,nums[%d]=%d\n"%(i,nums[i],l,nums[l],r,nums[r]))
                s = nums[i] + nums[l] + nums[r]
                if s < 0:
                    l +=1 
                elif s > 0:
                    r -= 1
                else:
                    res.append((nums[i], nums[l], nums[r]))
                    while l < r and nums[l] == nums[l+1]:
                        l += 1
                    while l < r and nums[r] == nums[r-1]:
                        r -= 1
                    l += 1; r -= 1
        return res
        
    

example=Solution()
print(example.threeSum([-1, 0, 1, 2, -1, -4]))  