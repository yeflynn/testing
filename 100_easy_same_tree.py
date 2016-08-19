#!/usr/bin/env python

#
# Given two binary trees, write a function to check if they are equal or not.
#
# Two binary trees are considered equal if they are structurally identical and the nodes have the same value.


# Analysis:
# Recrusion is simple if complexity is not a concern!
# Otherwise, has to traverse the tree in a loop with the help from a stack
# comparing only the current node value is not sufficient sicne None-1-2 matches 2-1-None in that case
# So must check left_val, cur_val, right_val

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def isSameTree(self, p, q):
        """
        :type p: TreeNode
        :type q: TreeNode
        :rtype: bool
        """
        if p == None and q == None:
            return True
        if p == None or q == None:
            return False

        stack1 = [p]
        stack2 = [q]
        while True:
            if len(stack1) != len(stack2):
                return False

            if len(stack1) == len(stack2) == 0:
                return True

            (values1, stack1) = self.PopAndProcess(stack1)
            (values2, stack2) = self.PopAndProcess(stack2)
            if values1 != values2:
                return False

    def PopAndProcess(self, stack):
        """
        stack is ensured to have >= 1 elements
        returns a tuple of (left, self, right) values
        """
        n = stack.pop()
        val = n.val
        lval = rval = None
        if n.left != None:
            lval = n.left.val
            stack.append(n.left)
        if n.right != None:
            rval = n.right.val
            stack.append(n.right)
        return ([lval, val, rval], stack)
