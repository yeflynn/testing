#!/usr/bin/env python

#  Write a program to check whether a given number is an ugly number.
#
# Ugly numbers are positive numbers whose prime factors only include 2, 3, 5.
# For example, 6, 8 are ugly while 14 is not ugly since it includes another prime factor 7.
#
# Note that 1 is typically treated as an ugly number.

# Use mod, %

 class Solution:
    # @param {integer} num
    # @return {boolean}
    def isUgly(self, num):
        while True:
            tmp = num
            for x in [2, 3, 5]:
                if num % x == 0:
                    num = int(num/x)
            if tmp == num:
                break
        return num == 1


if __name__ == '__main__':
