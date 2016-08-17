#!/usr/bin/env python


# LeetCode 342. Power of Four
#
# Given an integer (signed 32 bits), write a function to check whether it is a power of 4.
#
# Example:
# Given num = 16, return true. Given num = 5, return false.
#
# Follow up: Could you solve it without loops/recursion?

# Power of 4
#
# Highest bit must be 1
#
# Even number of trailing 0s in binary mode
#
# corner case is 0


class Solution(object):
    def isPowerOfFour(self, num):
        """
        :type num: int
        :rtype: bool
        """
        num = int(num)
        if num == 0:
            return False

        if num & (num - 1) != 0:
            return False

        num_trailing_zeros = 0
        tester = 1
        # Check bit by bit starting from the lowest
        while True:
            if (num & tester) != 0:
                # the bit is not 0
                if num > tester:
                    return False
                else:
                    break
            num_trailing_zeros += 1
            tester = int(tester * 2)

        if num_trailing_zeros % 2 == 1:
            return False
        else:
            return True

if __name__ == "__main__":
    sol = Solution()
    print(sol.isPowerOfFour(4))
    print(sol.isPowerOfFour(0))
