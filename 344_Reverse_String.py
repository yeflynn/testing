#!/usr/bin/env python


# Write a function that takes a string as input and returns the string reversed.
#
# Example:
# Given s = "hello", return "olleh".

class Solution(object):
    def reverseString(self, s):
        """
        :type s: str
        :rtype: str
        """
        # traverse string as a char list backward
        # pay attention to index start and end boundries.
        ret = []
        for index in xrange(len(s)-1, -1, -1):
          ret.append(s[index])

        return ''.join(ret)

if __name__ == "__main__":
    solution = Solution()
    print solution.reverseString("hello")
