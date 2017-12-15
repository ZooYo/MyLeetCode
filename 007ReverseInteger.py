'''
Created on 2017年2月25日

@author: Luke
'''

class Solution(object):
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        if x>0:
            nstr=str(x)[::-1]
            if int(nstr)<2147483648:
                return int(nstr)
            else:
                return 0
        else:
            x=abs(x)
            nstr=str(x)[::-1]
            if int(nstr)*-1>-2147483648:
                return int(nstr)*-1
            else:
                return 0


example=Solution()
print(example.reverse(-2147483648))