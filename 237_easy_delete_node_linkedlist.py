#!/usr/bin/env python


#  Write a function to delete a node (except the tail) in a singly linked list, given only access to that node.
#
# Supposed the linked list is 1 -> 2 -> 3 -> 4 and you are given the third node with value 3,
# the linked list should become 1 -> 2 -> 4 after calling your function.

# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    # @param {ListNode} node
    # @return {void} Do not return anything, modify node in-place instead.
    def deleteNode(self, node):
        if node.next is not None:
            node.val, node.next = node.next.val, node.next.next
        else:
            node = None

def PrintList(root):
    ret = []
    n = root
    while n is not None:
        ret.append(str(n.val))
        n = n.next
    print("->".join(ret))

if __name__ == '__main__':
    n1 = ListNode(1)
    n2 = ListNode(2)
    n3 = ListNode(3)
    n4 = ListNode(4)
    n1.next = n2
    n2.next = n3
    n3.next = n4

    PrintList(n1)
    sol = Solution()
    sol.deleteNode(n3)
    PrintList(n1)
