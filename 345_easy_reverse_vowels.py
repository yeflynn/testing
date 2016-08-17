#!/usr/bin/env python


# Write a function that takes a string as input and reverse only the vowels of a string.
#
# Example 1:
#
# Given s = "hello", return "holle".
#
# Example 2:
#
# Given s = "leetcode", return "leotcede".


# Scan twice
class Solution(object):
    def reverseVowels(self, s):
        """
        :type s: str
        :rtype: str
        """
        VOWELS = ('a', 'e', 'i', 'o', 'u','A','E','I','O','U')
        # Scan twice
        v = []
        for c in s:
            if c in VOWELS:
                v.append(c)

        ret = []
        for c in s:
            if c in VOWELS:
                ret.append(v.pop())
            else:
                ret.append(c)

        return ''.join(ret)


if __name__ == "__main__":
    s = "leetcode"
    print("test string " + s)
    sol = Solution()
    print(sol.reverseVowels(s))

    s = "aA"
    print("test string " + s)
    sol = Solution()
    print(sol.reverseVowels(s))
