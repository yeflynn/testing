#!/usr/bin/env python


#  Given a binary search tree (BST), find the lowest common ancestor (LCA) of two given nodes in the BST.
#
# According to the definition of LCA on Wikipedia: “The lowest common ancestor is
# defined between two nodes v and w as the lowest node in T that has both v and w as
# descendants (where we allow a node to be a descendant of itself).”
#
#         _______6______
#        /              \
#     ___2__          ___8__
#    /      \        /      \
#    0      _4       7       9
#          /  \
#          3   5
# For example, the lowest common ancestor (LCA) of nodes 2 and 8 is 6. Another
# example is LCA of nodes 2 and 4 is 2, since a node can be a descendant of itself
# according to the LCA definition.
#

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

# Comment: Use the character of BST
class Solution:
    # @param {TreeNode} root
    # @param {TreeNode} p
    # @param {TreeNode} q
    # @return {TreeNode}
    def lowestCommonAncestor(self, root, p, q):
        while (root.val - p.val) * (root.val - q.val) > 0:
            # 2 nodes are at the same side of root
            if root.val - p.val > 0:
                root = root.left
            else:
                root = root.right

        # if 2 nodes are at the different sides of root, then root is the LCA
        return root


if __name__ == '__main__':
