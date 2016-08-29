#!/usr/bin/env python


#  Given two strings s and t, write a function to determine if t is an anagram of s.
#
# For example,
# s = "anagram", t = "nagaram", return true.
# s = "rat", t = "car", return false.
#
# Note:
#
# You may assume the string contains only lowercase alphabets.

class Solution:
    # @param {string} s
    # @param {string} t
    # @return {boolean}

    # Solution #1:  sort and compare, 2NlogN + N
    def isAnagram(self, s, t):
        s1 = sorted(s)
        t1 = sorted(t)
        return s1 == t1

    # Solution #2: use hash, O(N)
    def isAnagram2(self, s, t):
        d = {}
        for x in s:
            if d.get(x) is None:
                d[x] = 1
            else:
                d[x] += 1
        print(d)

        for y in t:
            print(d)
            if d.get(y) is None or d.get(y) == 0:
                return False
            else:
                d[y] -= 1

        if sum(d.values()) is not 0:
            return False

        return True


if __name__ == '__main__':
    s = "anagram"
    t = "nagaram"
    sol = Solution()
    print("%s, %s, %d" %(s, t, sol.isAnagram2(s,t)))

    s = "aacc"
    t = "ccac"
    sol = Solution()
    print("%s, %s, %d" %(s, t, sol.isAnagram2(s,t)))
