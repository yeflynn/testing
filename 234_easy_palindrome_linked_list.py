#!/usr/bin/env python

# Given a singly linked list, determine if it is a palindrome.
#
# 1->2->2->1
# 1->2->1
# 1->2->3->2->1
# Follow up:
# Could you do it in O(n) time and O(1) space?

import math
# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    # @param {ListNode} head
    # @return {boolean}

    # Comment:
    # 1. Use slow and faster pointers to find mid point. Be careful about the odd and even list
    #    For odd, slow points to mid when fast points to last
    #    For even, slow points to mid-left, when fast points to last
    # 2. Reverse 2nd half
    def isPalindrome(self, head):
        if head is None or head.next is None:
            return True

        slow = head
        fast = head
        is_even = False
        while fast.next is not None:
            fast = fast.next
            if fast.next is None:  # This handles even and odd list
                is_even = True
                break
            else:
                fast = fast.next
            slow = slow.next

        # Reverse 2nd half in-place
        head2 = self.reverseList(slow.next)

        # If odd, compare [0, mid-1] vs. [head2, :]
        # If even, compare [0, mid-left] vs. [head2, :]
        # We shouldn't care, since length is limited by [head2, :]
        return self.compareLists(head2, head)

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

    def compareLists(self, h1, h2):
        while h1 is not None:
            if h1.val != h2.val:
                return False
            h1 = h1.next
            h2 = h2.next
        return True






    # Comment: Use a stack, O(2N) time, O(N) space
    def isPalindrome2(self, head):
        if head is None or head.next is None:
            return True

        l = 0
        n = head
        linked_list = []
        while n is not None:
            linked_list.append(str(n.val))
            l += 1
            n = n.next

        # print("->".join(linked_list))
        n = head
        tmp = []
        # For even list    0,..., l/2-1   vs. l/2, l/2+1, ..., l-1
        # For one node list, return True
        # For odd list     0,..., floor(l/2)-1,  (skip floor(l/2))  floor(l/2)+1, ..., l-1
        for index in range(0, l):
            if index < math.floor(l/2):
                tmp.append(n.val)
            else:
                if (l % 2) == 1 and index == math.floor(l/2):
                    # print("skip %d" % n.val)
                    n = n.next
                    continue
                expected = tmp.pop()
                # print("exp %d, val %d" % (expected, n.val))
                if expected != n.val:
                    return False
            n = n.next
        return True



if __name__ == '__main__':
    n1 = ListNode(1)
    n2 = ListNode(2)
    n3 = ListNode(2)
    n4 = ListNode(1)
    n1.next = n2
    n2.next = n3
    n3.next = n4

    sol = Solution()
    print(sol.isPalindrome(n2))
    print(sol.isPalindrome(n1))
