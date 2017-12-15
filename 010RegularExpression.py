'''
Created on 2017年2月27日

@author: Luke
'''

class Solution(object):
    def isMatch(self, s, p):
        # The DP table and the string s and p use the same indexes i and j, but
        # table[i][j] means the match status between p[:i] and s[:j], i.e.
        # table[0][0] means the match status of two empty strings, and
        # table[1][1] means the match status of p[0] and s[0]. Therefore, when
        # refering to the i-th and the j-th characters of p and s for updating
        # table[i][j], we use p[i - 1] and s[j - 1].

        # Initialize the table with False. The first row is satisfied.
        table = [[False] * (len(s) + 1) for _ in range(len(p) + 1)]

        # Update the corner case of matching two empty strings.
        table[0][0] = True
        print(table)
        # Update the corner case of when s is an empty string but p is not.
        # Since each '*' can eliminate the charter before it, the table is
        # vertically updated by the one before previous. [test_symbol_0]
        for i in range(2, len(p) + 1):
            table[i][0] = table[i - 2][0] and p[i - 1] == '*'

        for i in range(1, len(p) + 1):
            for j in range(1, len(s) + 1):
                if p[i - 1] != "*":
                    # Update the table by referring the diagonal element.
                    table[i][j] = table[i - 1][j - 1] and \
                                  (p[i - 1] == s[j - 1] or p[i - 1] == '.')
                    print("table[%d][%d]=%r"%(i,j,table[i][j]))
                else:
                    # Eliminations (referring to the vertical element)
                    # Either refer to the one before previous or the previous.
                    # I.e. * eliminate the previous or count the previous.
                    # [test_symbol_1]
                    table[i][j] = table[i - 2][j] or table[i - 1][j]
                    print()
                    print("table[%d][%d]=%r"%(i,j,table[i][j]))
                    print("table [i-2=%d][j=%d]=%r"%(i-2,j,table[i-2][j]))
                    print("table [i-1=%d][j=%d]=%r"%(i-1,j,table[i-1][j]))
                    # Propagations (referring to the horizontal element)
                    # If p's previous one is equal to the current s, with
                    # helps of *, the status can be propagated from the left.
                    # [test_symbol_2]
                    print("p[i - 2]=%s"%p[i-2])
                    print("s[j - 1]=%s"%s[j - 1])
                    if p[i - 2] == s[j - 1] or p[i - 2] == '.':
                        table[i][j] |= table[i][j - 1]
                        print("table[%d][%d]=%r"%(i,j,table[i][j]))
                        print("table[%d][%d]=%r"%(i,j-1,table[i][j]))
        print(table)                
        return table[-1][-1]
        

example=Solution()
#print(example.isMatch("baaaa","baaaa"))
print(example.isMatch("baaaabb","ba*"))