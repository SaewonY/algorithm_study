# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        carry = 0
        res = n = ListNode(0)
        
        while 11 or l2 or carry:
            if l1:
                carry += l1.val
                l1 = l1.next
        print(carry)


input1 = [2, 4, 3]
input2 = [5, 6, 4]
A = Solution()
A.addTwoNumbers(input1, input2)
