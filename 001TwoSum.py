'''
Created on 2017年2月20日 

@author: Luke
Given nums = [2, 7, 11, 15], target = 9,

Because nums[0] + nums[1] = 2 + 7 = 9,
return [0, 1].
'''
"""
class Solution(object):
    
    def twoSum(self, nums, target):
        
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        
        for i in range(0,len(nums),1):        #將Nums內的數字組合比對，若與Target相等則加入至list並將list回傳
            for j in range(i+1,len(nums),1):
                if nums[i]+nums[j]==target:
                    list=[]
                    list.append(i)
                    list.append(j)
                    return list

    """
    
class Solution(object):               #設A+B=9，利用9-A=B的規則，若已將A:i放入，則9-B在index
    def twoSum(self, nums, target):  
        index = {}
        for i, x in enumerate(nums):
            #print ("i=%d"%i)
            #print ("x=%d"%x)
            #print ("t-x=%d"%(target-x))
            #print (index)
            if target - x in index:
                return [index[target - x], i]
            index[x] = i
            #print (index)
    
example=Solution()
print (example.twoSum([15, 7, 11, 2],9))