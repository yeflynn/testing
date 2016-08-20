#!/usr/bin/env python


# Given a binary tree, find its minimum depth.
#
# The minimum depth is the number of nodes along the shortest path from the root node down to the nearest leaf node.



# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


# BFS or DFS
class Solution(object):
    # Recursion
    # Pay attention to 2 cases
    # - if a node has both left and right children, the min depth is 1 + min(d_left, d_right)
    # - if a node is missing one of child or both, the min depth is 1 + max(d_left, d_right)
    #   simply because a node missing one child is not a leaf node.
    def minDepth(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if root == None:
            return 0
        if root.left == None or root.right == None:
            return 1 + max(self.minDepth(root.left), self.minDepth(root.right))
        return 1 + min(self.minDepth(root.left), self.minDepth(root.right))

    # DFS
    # Use stack = [(node, depth)] to do DFS
    # while stack is not empty, keep going
    # if hit leaf node, check depth vs. min_depth
    # if hit non-leaf node, push back (left, depth+1) and (right, depth+1)
    def minDepth(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if root == None:
            return 0
        min_d = 99999
        stack = [(root, 1)]
        while len(stack) > 0:
            n, d = stack.pop()
            if n.left == None and n.right == None:  # this is a leaf
                min_d = min(min_d, d)
            if n.right != None:
                stack.append((n.right, d+1))
            if n.left != None:
                stack.append((n.left, d+1))
        return min_d

    # BFS
    # use queue = [node] to do BFS
    # Each time add the entire +1 layer (all children from nodes in upper layer) to the queue
    # The first leaf node hit has the min depth
    import Queue
    def minDepth(self, root):
        if root == None:
            return 0
        q = Queue.Queue()
        q.put((root, 1))
        while True:
            n, d = q.get_nowait()
            if n.left == None and n.right == None:
                # n is a leaf node
                return d
            if n.left != None:
                q.put((n.left, d+1))
            if n.right != None:
                q.put((n.right, d+1))
