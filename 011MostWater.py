'''
Created on 2017年2月28日

@author: Luke
'''
'''
class Solution(object):
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        if(len(height)<=2):
            return min(height)
        nheight=sorted(height)
        area=nheight[0]*len(height)-1
        for i,item in enumerate(nheight[0:len(height)],0):
            #print("nheight[%d]=%d"%(i,nheight[i]))
            if nheight[i]!=nheight[i-1]:
                height_index=height.index(item)
            else:
                #print("nheight[%d]=%d"%(i,nheight[i]))
                #print("height_index=%d,item=%d"%(height_index,item))
                height_index=height[height_index+1:len(height)].index(item)+height_index+1
                #print("height_index=%d,item=%d"%(height_index,item))
            far_index=0
            for j in range(len(height)):
               # print("height_index=%d,j=%d\n"%(height_index,j))
                if(height[height_index]<=height[j]):
                    far_index=max(far_index,abs(height_index-j))          
                #print("item=%d,far_index=%d"%(item,far_index))
            area=max(area,far_index*item)
            #print("area=%d"%area)
        return area
'''
class Solution(object):
    def maxArea(self, height):
        max_area = area = 0
        left, right = 0, len(height) - 1
        while left < right:
            l, r = height[left], height[right]
            if l < r:
                area = (right - left) * l
                while height[left] <= l:
                    left += 1
            else:
                area = (right - left) * r
                while height[right] <= r and right:
                    right -= 1
            if area > max_area:
                max_area = area
        return max_area

example=Solution()
#print(example.maxArea([1, 2, 13, 14, 5, 6]))
#print(example.maxArea([0,2]))
#print(example.maxArea([3,2,1,3]))
print(example.maxArea([0,14,6,2,10,9,4,1,10,3]))
#print(example.maxArea([1,2,1]))
#print(example.maxArea([1,3,2,5,25,24,5]))
#l1=[0,1,2,3,4,5,6,7,8,9]
#print(l1[4:9].index(7)+4)

