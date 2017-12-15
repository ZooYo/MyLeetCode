'''
Created on 2017年2月26日

@author: Luke
'''
'''
class Solution(object):
    def myAtoi(self, str):
        """
        :type str: str
        :rtype: int
        """
        times=1
        num=0
        nstr=str[1:len(str)][::-1]
        for i in range(0,len(str)-1):
            num+=int(nstr[i])*times
            times*=10
        if(str[0])=="+":
            return num
        else:
            return num*-1
'''
class Solution(object):
    def myAtoi(self, s):
        ###better to do strip before sanity check (although 8ms slower):
        #ls = list(s.strip())
        #if len(ls) == 0 : return 0
        if len(s) == 0 : return 0
        ls = list(s.strip())
        sign = -1 if ls[0] == '-' else 1 #正=1，負=-1
        if ls[0] in ['-','+'] : del ls[0] #將正負號刪除
        ret, i = 0, 0
        while i < len(ls) and ls[i].isdigit() :
            ret = ret*10 + ord(ls[i]) - ord('0') #將數字相加後進一位，重複
            i += 1
        return max(-2**31, min(sign * ret,2**31-1))
example=Solution()
print(example.myAtoi("-125643"))