#!/usr/bin/env python

# Given a pattern and a string str, find if str follows the same pattern.
#
# Examples:
#
# pattern = "abba", str = "dog cat cat dog" should return true.
# pattern = "abba", str = "dog cat cat fish" should return false.
# pattern = "aaaa", str = "dog cat cat dog" should return false.
# pattern = "abba", str = "dog dog dog dog" should return false.
#
# Notes:
#
# Both pattern and str contains only lowercase alphabetical letters.
# Both pattern and str do not have leading or trailing spaces.
# Each word in str is separated by a single space.
# Each letter in pattern must map to a word with length that is at least 1.


# Use a map (hash_map, unordered_map) is the best to do pattern match
class Solution(object):
    def wordPattern(self, pattern, str):
        """
        :type pattern: str
        :type str: str
        :rtype: bool
        """
        p = []
        for c in pattern:
            p.append(c)
        s = str.split(' ')
        # One can compute fingerprint for each string to reduce complexity during comparison
        if len(p) != len(s):
            return False

        m = {}
        tmp = set()
        for index in range(0, len(p)):
            if not m.has_key(p[index]):  # p[index] is a new val first seen in p
                if s[index] in tmp:  # s[index] is not a new val first seen in s
                    return False
                else:
                    m.update({p[index] : s[index]})
                    tmp.add(s[index])
            else:
                if m[p[index]] != s[index]:
                    return False
        return True
