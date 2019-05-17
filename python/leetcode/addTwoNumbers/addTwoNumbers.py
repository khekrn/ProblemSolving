'''
You are given two non-empty linked lists representing two non-negative integers. The digits are stored in reverse order and each of their nodes contain a single digit. Add the two numbers and return it as a linked list.

You may assume the two numbers do not contain any leading zero, except the number 0 itself.

Example:

Input: (2 -> 4 -> 3) + (5 -> 6 -> 4)
Output: 7 -> 0 -> 8
Explanation: 342 + 465 = 807.
'''


# Definition for singly-linked list.
from collections import deque


class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:

    def convert(self, list):
        res = int("".join(map(str, list)))
        return res

    def get_value(self, l1):
        values = deque()
        current = l1
        while current != None:
            values.appendleft(current.val)
            current = current.next
        return self.convert(values)
    
    def list2link(self, l):
        if len(l) == 0:
            return None
        ret_tail = ret_head = ListNode(l[0])
        for val in l[1:]:
            tmp = ListNode(val)
            ret_tail.next = tmp
            ret_tail = ret_tail.next
        return ret_head

    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        if l1 == None:
            return l2
        if l2 == None:
            return l1
        l1_res = self.get_value(l1)
        l2_res = self.get_value(l2)
        res = l1_res+l2_res
        res_list = [int(i) for i in str(res)]
        return self.list2link(res_list[::-1])


[2,4,3]
[5,6,4]

l1 = ListNode(2)
l2 = ListNode(4)
l3 = ListNode(3)

l1.next = l2
l2.next = l3

l4 = ListNode(5)
aa = ListNode(6)
bb = ListNode(4)

l4.next = aa
aa.next = bb

sol = Solution()
res = sol.addTwoNumbers(l1, l4)
print(res.val)
print(res.next.val)
print(res.next.next.val)

def print_link(link):
    while link is not None:
        print(link.val, link, "=", link.next)
    print("\n")

#print(print_link(res))