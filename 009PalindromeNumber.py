'''
Created on 2017年2月27日

@author: Luke
'''

class Solution(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        nstr=str(x)
        for i in range(len(nstr)//2):
            if not nstr[i]==nstr[len(nstr)-i-1]:
                return False
        return True
example=Solution()
print(example.isPalindrome(12321))