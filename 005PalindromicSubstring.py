'''
Created on 2017年2月23日

@author: Luke
'''
from pip._vendor.requests.packages.urllib3.connectionpool import xrange
'''
Example:
Input: "babad"
Output: "bab"

Note: "aba" is also a valid answer.

Example:
Input: "cbbd"
Output: "bb"

'''
'''
class Solution(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        longest=0
        longpalind=""
        for i in range(len(s)):
            end=len(s)-1
            while (end-i+1>longest):
                if self.palindrome(s[i:end+1]):
                    if longest<end-i+1:
                        longest=end-i+1
                        longpalind=s[i:end+1]                
                end-=1
        return longpalind
    
    def palindrome(self,s):
        for i in range(len(s)):
            if s[i]!=s[len(s)-i-1]:
                return False
        return True
'''
class Solution:
    def longestPalindrome(self, s):
        if len(s)==0:
            return 0
        maxLen=1
        start=0
        for i in xrange(len(s)):
            print("-------------")
            print("i=%d"%i)
            print("not yet=%s"%s[i-maxLen:i+1])
            print("i-maxLen=%d"%(i-maxLen))
            if i-maxLen >=1 and s[i-maxLen-1:i+1]==s[i-maxLen-1:i+1][::-1]: #s[i-maxLen-1:i+1]==s[i-maxLen-1:i+1][::-1]判斷迴文
                print(">=1,%s"%s[i-maxLen:i+1])
                start=i-maxLen-1
                maxLen+=2
                print("start=%d"%start)
                print("maxLen=%d"%maxLen)
                print("thing_return=%s"%s[start:start+maxLen])
                continue

            if i-maxLen >=0 and s[i-maxLen:i+1]==s[i-maxLen:i+1][::-1]:
                print(">=0,%s"%s[i-maxLen:i+1])
                start=i-maxLen
                maxLen+=1
            print("start=%d"%start)
            print("maxLen=%d"%maxLen)
            print("thing_return=%s"%s[start:start+maxLen])
        return s[start:start+maxLen]

example=Solution()
print(example.longestPalindrome("abacbaqwertrewqjackcajmnop"))
