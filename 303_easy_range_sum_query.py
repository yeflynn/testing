#!/usr/bin/env python
# Given an integer array nums, find the sum of the elements between indices i and j (i <= j), inclusive.
#
# Example:
#
# Given nums = [-2, 0, 3, -5, 2, -1]
#
# sumRange(0, 2) -> 1
# sumRange(2, 5) -> -1
# sumRange(0, 5) -> -3
# Note:
#
# You may assume that the array does not change.
# There are many calls to sumRange function.

# Analysis
# This can be solved directed by calling sum(nums[i:j+1]) for every call
# Another faster solution is to precompute sum for [0,1], [0,2], ..., [0,n-1]
# and any range [i,j] can be computed from [0,j] - [0,i-1]
# Lots of corner cases!!!!

class NumArray(object):
    def __init__(self, nums):
        """
        initialize your data structure here.
        :type nums: List[int]
        """
        N = len(nums)
        self.max_index = N - 1
        if N == 0:
            self.sums = []
        else:
            # Compute sum for [0,0], [0,1], ..., [0,N-1]
            self.sums = [0] * N
            self.sums[0] = nums[0]
            if N >= 2:
                for k in range(1, N):
                    self.sums[k] = self.sums[k-1] + nums[k]

    def sumRange(self, i, j):
        """
        sum of elements nums[i..j], inclusive.
        :type i: int
        :type j: int
        :rtype: int
        """
        if i < 0 or i > j or j > self.max_index:
            print("Fatal: invalid index range")
            return None

        if i == 0:
            return self.sums[j]
        else:
            return self.sums[j] - self.sums[i-1]


# Your NumArray object will be instantiated and called as such:
# numArray = NumArray(nums)
# numArray.sumRange(0, 1)
# numArray.sumRange(1, 2)

if __name__ == "__main__":
    test1 = NumArray([1])
    print test1.sumRange(0,0)

    test2 = NumArray([1,1,1,1])
    print test2.sumRange(0,0)
    print test2.sumRange(0,1)
    print test2.sumRange(0,3)
    print test2.sumRange(1,3)
    print test2.sumRange(2,3)

    test3 = NumArray([])
    print test3.sumRange(0,0)
