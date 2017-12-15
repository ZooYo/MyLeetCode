'''
Created on 2017年3月6日

@author: Luke
'''
'''
利用左減右家的方式搭配字典逐字轉為數字後相加
'''
'''
class Solution(object):
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """
        int_dic={'M': 1000,'D': 500 ,'C': 100,'L': 50,'X': 10,'V': 5,'I': 1}
        num=0
        for i in range(len(s)):
            #print(int_dic[s[i]])
            #print (num)
            if  i==len(s)-1:
                num+=int_dic[s[i]]
            elif int_dic[s[i]]>=int_dic[s[i+1]]:
                num+=int_dic[s[i]]
            else:
                num-=int_dic[s[i]]    
        return num
'''
'''
由右往左數，由d[p]儲存上個英文字代表位數，並做d[c]小於<d[p]來判斷數字的加減
'''
class Solution(object):
    def romanToInt(self, s):
        d = {'M':1000, 'D':500, 'C':100, 'L':50, 'X':10, 'V':5, 'I':1}
        res, p = 0, 'I'
        for c in s[::-1]:
            print("before:")
            print("res=%d"%res)
            print("p=%s"%p)
            print("d[c]=%d"%d[c])
            print("d[p]=%d\n"%d[p])
            res, p = res - d[c] if d[c] < d[p] else res + d[c], c
            print("after:")
            print("res=%d"%res)
            print("p=%s\n"%p)
        return res

example=Solution()
print(example.romanToInt("MMCDLXIX"))    