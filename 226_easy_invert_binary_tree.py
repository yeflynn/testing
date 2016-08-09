#!/usr/bin/env python

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, value, left_child=None, right_child=None):
        """
        value: value of the tree node.
        left_child: left child TreeNode object
        right_child: right child TreeNode object
        """
        self.value = value
        self.lc = left_child
        self.rc = right_child

class Solution:
    # @param {TreeNode} root
    # @return {TreeNode}
    # Recursion solution
    @classmethod
    def invertTree(cls, root):
        # End criteria
        if root == None:
            return None

        tmp = root.lc
        root.lc = root.rc
        root.rc = tmp

        cls.invertTree(root.lc)
        cls.invertTree(root.rc)

    # None recursion
    @classmethod
    def invertTree2(cls, root):
        # End criteria
        if root == None:
            return None

        # Probably do not need a formal stack, a list serving as an FIFO queue is sufficient.
        node_list = [root]
        while len(node_list):
            n = node_list[0]
            tmp = n.lc
            n.lc = n.rc
            n.rc = tmp
            if n.lc != None:
                node_list.append(n.lc)
            if n.rc != None:
                node_list.append(n.rc)

            node_list = node_list[1:]


def BreadthFirstPrint(siblings):
    """
    BFS to print a binary tree. Node defined by TreeNode.
    To bootstrap this, use input siblings=[root]
    """
    cur_layer_output = []
    new_siblings = []
    for node in siblings:
        if node == None:
            continue
        lc = -1
        rc = -1
        if node.lc != None:
            lc = node.lc.value
            new_siblings.append(node.lc)
        if node.rc != None:
            rc = node.rc.value
            new_siblings.append(node.rc)

        cur_layer_output.append("%4d : [%4d] : %4d" % (lc, node.value, rc))

    print(",    ".join(cur_layer_output))
    if len(new_siblings) > 0:
        BreadthFirstPrint(new_siblings)


if __name__ == "__main__":
    print("Test case, define tree node as n_ab where a is the depth, and b is the sequence from left to right (asc ordering) within a layer")
    #      4
    #    2     5
    #  1    3
    n21 = TreeNode(1)
    n22 = TreeNode(3)
    n11 = TreeNode(2, n21, n22)
    n12 = TreeNode(5)
    n0 = TreeNode(4, n11, n12)

    print("Original tree:")
    BreadthFirstPrint([n0])

    Solution.invertTree(n0)
    print("Inverted tree:")
    BreadthFirstPrint([n0])

    Solution.invertTree2(n0)
    print("ReInverted tree:")
    BreadthFirstPrint([n0])
