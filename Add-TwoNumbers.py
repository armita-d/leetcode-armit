'''
You are given two non-empty linked lists representing two non-negative integers. The digits are stored in reverse order, and each of their nodes contains a single digit. Add the two numbers and return the sum as a linked list.

You may assume the two numbers do not contain any leading zero, except the number 0 itself.

 Example 1:
 Input: l1 = [2,4,3], l2 = [5,6,4]
Output: [7,0,8]
Explanation: 342 + 465 = 807.

'''
# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
         self.val = val
         self.next = next
class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: Optional[ListNode]
        :type l2: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        carry = 0
        head = ListNode(0)
        current = 0
        
        while l1 is not None or l2 is not None or carry != 0:
            val1 = l1.val if val1 is not None else 0
            val2 = l2.val if val2 is not None else 0
            total= val1 + val2 + carry

            new_digit = total % 10
            carry = total // 10

            current.next = ListNode(new_digit)
            current = current.next

            if l1 is not None:
                l1 = l1.next

            if l2 is not None:
                l2 = l2.next

        return head.next #b/c we have ListNode(0) and it's 0 but we dont have it we just made it so at the end we have to return head.next and not head(This means head holds a dummy node with value 0 that is not part of the real answer.
#We only use it to make building the list easier.) 



