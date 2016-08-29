#!/usr/bin/env python


# Given a binary tree, return all root-to-leaf paths.
#
# For example, given the following binary tree:
#
#    1
#  /   \
# 2     3
#  \
#   5
# All root-to-leaf paths are:
#
# ["1->2->5", "1->3"]

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

# Comment:  use DFS, need a stack
class Solution:
    # @param {TreeNode} root
    # @return {string[]}
    def binaryTreePaths(self, root):
        ret = []
        if root is None:
            return ret

        nodes_todo = [(root, "")]
        while len(nodes_todo) > 0:
            n, prefix = nodes_todo.pop()   # Get the last enqued element, stack
            if n.left is None and n.right is None:
                path = ("%s%d" % (prefix, n.val))
                ret.append(path)
            else:
                pre = ("%s%d->" % (prefix, n.val))
                if n.left is not None:
                    nodes_todo.append((n.left, pre))
                if n.right is not None:
                    nodes_todo.append((n.right, pre))
        return ret



if __name__ == '__main__':
