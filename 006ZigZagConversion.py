'''
Created on 2017年2月24日

@author: Luke
'''
'''
class Solution(object):
    def convert(self, s, numRows):
        ns=""
        if len(s)<=numRows or numRows==1:
            return s
        if numRows==2:
            ns+=(s[0:len(s):2])
            ns+=(s[1:len(s):2])
            return ns
        for i in range(numRows): #利用歸納法數學上的對稱
            n=i
            while n <len(s):
                ns+=s[n]       
                if n+(numRows-i-1)*2>=len(s):
                    break
                if i !=0 and i!=numRows-1:
                    ns+=s[n+(numRows-i-1)*2]
                n+=2*numRows-2  
                    
        return ns
'''
class Solution(object):
    def convert(self, s, numRows): #利用來回移動在INDEX內加入string內容
        if numRows == 1 or numRows >= len(s):
            return s

        L = [''] * numRows
        index, step = 0, 1

        for x in s:
            L[index] += x
            print(L)
            if index == 0:
                step = 1
            elif index == numRows -1:
                step = -1
            index += step

        return ''.join(L)
             
example=Solution()
print(example.convert("ABCDEF",4))
