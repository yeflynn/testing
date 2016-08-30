#!/usr/bin/env python


# Find the total area covered by two rectilinear rectangles in a 2D plane.
#
# Each rectangle is defined by its bottom left corner and top right corner as shown in the figure.
#
# [LeetCode]Rectangle Area
#    CD
# AB
#
#    GH
# EF
# Assume that the total area is never beyond the maximum possible value of int.

# Comment: There is a total of 4 possible interception patterns
# All interception area can be described by rec (max(A,E), max(B,F)) (min(C,G), min(D,H))
# Tricky part: negative length means no intersection
class Solution:
    # @param {integer} A
    # @param {integer} B
    # @param {integer} C
    # @param {integer} D
    # @param {integer} E
    # @param {integer} F
    # @param {integer} G
    # @param {integer} H
    # @return {integer}
    def computeArea(self, A, B, C, D, E, F, G, H):
        return (C-A) * (D-B) + (G-E) * (H-F) - max(0, min(C,G)-max(A,E)) * max(0, (min(D,H)-max(B,F)))



if __name__ == '__main__':
