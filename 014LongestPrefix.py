'''
Created on 2017年3月7日

@author: Luke
'''


class Solution(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        if not strs:
            return ""
        shortest = min(strs,key=len)
        print(shortest)
        for i, ch in enumerate(shortest):
            #print("i=%d,ch=%s"%(i,ch))
            for other in strs:
                #print("other=%s"%other)
                #print("other[%d]=%s"%(i,other[i]))
                if other[i] != ch:
                    return shortest[:i]
        return shortest 

                
example=Solution()
print(example.longestCommonPrefix(["abcd","abcde","abca"]))        