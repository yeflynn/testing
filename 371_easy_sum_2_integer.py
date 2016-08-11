#!/usr/bin/env python


class Solution(object):
    def getSum(self, a, b):
        """
        :type a: int
        :type b: int
        :rtype: int
        Some common knowledge:
        let say int32, it has 32 bits, 0xffffffff
        hex(n & 0xffffffff) will give the hex representation of a number n
        The max int32 is 0x7fffffff
        The -1 is 0xffffffff, the largest negative number
        The -2 is 0xfffffffe
        The min int32 is 0x80000000
        """
