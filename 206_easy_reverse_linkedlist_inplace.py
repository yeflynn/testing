#!/usr/bin/env python


 # Reverse a singly linked list.

 # Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

# In place, O(N) time, O(1) space
# Need 3 points
class Solution:
    # @param {ListNode} head
    # @return {ListNode}
    def reverseList(self, head):
        if head is None or head.next is None:
            return head

        p = head
        last = None
        while p is not None:
            next = p.next
            p.next = last
            last = p
            p = next
        return last


if __name__ == '__main__':
