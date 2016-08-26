#!/usr/bin/env python

#  Given a non-negative integer num, repeatedly add all its digits until the result has only one digit.
#
# For example:
#
# Given num = 38, the process is like: 3 + 8 = 11, 1 + 1 = 2. Since 2 has only one digit, return it.
#
# Follow up:
#
# Could you do it without any loop/recursion in O(1) runtime?
#
# Hint:
#
# A naive implementation of the above process is trivial. Could you come up with other methods?
#
# What are all the possible results?
#
# How do they occur, periodically or randomly?
#

class Solution:
    # @param {integer} num
    # @return {integer}
    def addDigits(self, num):
        tmp = 0
        while num >= 10:
            tmp = tmp + num % 10
            num = int(num/10)
            if num < 10:
                tmp = tmp + num
                num = tmp
                tmp = 0

        return num

if __name__ == '__main__':
    sol = Solution()
    num = 12345  # 1+2+3+4+5 = 15 = 1+5 = 6
    print(num)
    print(sol.addDigits(num))
