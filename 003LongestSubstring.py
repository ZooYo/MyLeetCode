'''
Created on 2017年2月22日

@author: Luke
'''

'''
Given "abcabcbb", the answer is "abc", which the length is 3.
Given "bbbbb", the answer is "b", with the length of 1.
Given "pwwkew", the answer is "wke", with the length of 3. 
Note that the answer must be a substring, "pwke" is a subsequence and not a substring.
'''

class Solution(object):
    def lengthOfLongestSubstring(self, s):
        start = maxLength = 0
        usedChar = {}
        
        for i in range(len(s)):
            print("第%d次開始:%c in %s"%(i,s[i],usedChar))
            if s[i] in usedChar and start <= usedChar[s[i]]: #若文字重複且其位置大於等於目前起始位置時重製起始位置
                print("usedChar[s[i]]=%d"%usedChar[s[i]])
                start = usedChar[s[i]] + 1 #起始位置為上一個重複字的下一個索引值
            else:
                maxLength = max(maxLength, i - start + 1) #分析新的子字串長度是否較大

            usedChar[s[i]] = i #將文字逐一放入索引值
            print("第%d次結束:%c in %s"%(i,s[i],usedChar))
            print("usedChar[s[i]]=%d"%usedChar[s[i]])
            print ("start=%d"%start)
            print("maxLength=%d"%maxLength)
        return maxLength
example=Solution()
print (example.lengthOfLongestSubstring("abbabc"))  
    