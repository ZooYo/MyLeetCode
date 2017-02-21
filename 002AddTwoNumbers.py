'''
Created on 2017年2月21日

@author: Luke
You are given two non-empty linked lists representing two non-negative integers. 
The digits are stored in reverse order and each of their nodes contain a single digit.
 Add the two numbers and return it as a linked list.
You may assume the two numbers do not contain any leading zero, except the number 0 itself.
Input: (2 -> 4 -> 3) + (5 -> 6 -> 4)
Output: 7 -> 0 -> 8
'''
from xml.dom.minicompat import NodeList

# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None
'''
class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode 鏈結串列加法，由左至右做十進位加法，向右進位
        """
        if l1==None: return l2
        if l2==None: return l1
        carry=0
        dummy=ListNode(0)
        pointto=dummy
        while l1 and l2:
            pointto.next=ListNode((l1.val+l2.val+carry)%10)
            carry=(carry+l1.val+l2.val)/10
            l1=l1.next
            l2=l2.next
            pointto=pointto.next           
        if l2:
            while l2:
                pointto.next=ListNode((l2.val+carry)%10)
                carry=(carry+l2.val)/10
                l2=l2.next
                pointto=pointto.next  
        if l1:
            while l1:
                pointto.next=ListNode((l1.val+carry)%10)
                carry=(carry+l1.val)/10
                l1=l1.next
                pointto=pointto.next  
        if carry==1:
            pointto.next=ListNode(1)  
        return dummy.next  
'''
class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        ret = ListNode(0)
        cur = ret
        add = 0
        
        while l1 or l2 or add:#當鏈結串列或其進位不為0或空時:
            val = (l1.val if l1 else 0) + (l2.val if l2 else 0) + add
            add = val // 10
            cur.next = ListNode(val % 10)
            cur = cur.next
            l1 = l1.next if l1 else None
            l2 = l2.next if l2 else None
        
        return ret.next 

def PrintNodeList(nlist):
    while nlist:       
        nlist=nlist.next
        if not nlist.next: 
            print ("%d"%nlist.val)
            break
        print ("%d -> "%nlist.val, end='')       
def MakeNodeList():
    nlist=ListNode(0)
    nlistp=nlist
    datanum=int(input("請輸入資料筆數: "))
    for i in range(datanum):
        num=int(input("請輸入第%d個數字: "%(i+1)))
        nlistp.next=ListNode(num)
        nlistp=nlistp.next  
    PrintNodeList(nlist)  
    return nlist


list1=MakeNodeList()
list2=MakeNodeList()
example=Solution()
PrintNodeList(example.addTwoNumbers(list1,list2))
                
            