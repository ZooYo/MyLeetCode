'''
Created on 2017年3月12日

@author: Luke
'''
from _functools import reduce
'''
class Solution(object):
    def letterCombinations(self, digits):
        """
        :type digits: str
        :rtype: List[str]
        """
        dic={'2':"abc",'3':"def"}
        nlist=[]
        for i in range(len(digits)-1):
            for j in range(len(dic[digits[i]])):
                for k in range(len(dic[digits[i+1]])):
                    nlist.append(dic[digits[i]][j]+dic[digits[i+1]][k])
        return nlist
'''
'''
acc原為空的list
第一次結束後變為[''+y]=第一個digit的所有英文字
第二次則為第一個digit的所有英文字+第二個digit的英文字
'''
class Solution:
    def letterCombinations(self, digits):
        if '' == digits: return []
        kvmaps = {'2': 'abc','3': 'def','4': 'ghi','5': 'jkl','6': 'mno','7': 'pqrs','8': 'tuv','9': 'wxyz'}
        return reduce(lambda acc, digit:[x + y for x in acc for y in kvmaps[digit]], digits, [''])
example=Solution()
print(example.letterCombinations("234")) 