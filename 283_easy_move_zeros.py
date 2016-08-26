#!/usr/bin/env python

# Given an array nums, write a function to move all 0's to the end of it while
# maintaining the relative order of the non-zero elements.
#
# For example, given nums = [0, 1, 0, 3, 12], after calling your function, nums should be [1, 3, 12, 0, 0].
#
# Note:
#
# You must do this in-place without making a copy of the array.
# Minimize the total number of operations.


# Always switch the first 0 with the first non-zero after. This will group zeros together
# and move them towards the end one digit by one digit.
# Use y to point to the first 0
# Use x to point to the first non-zero after.

# python has easy way of swapping 2 vars

class Solution(object):
    def moveZeroes(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        y = 0
        for x in range(len(nums)):
            if nums[x]:
                nums[x], nums[y] = nums[y], nums[x]
                y += 1
        return nums




if __name__ == '__main__':
    nums = [0, 1, 1, 0, 0, 1, 1]
    print(nums)
    sol = Solution()
    print(sol.moveZeroes(nums))
