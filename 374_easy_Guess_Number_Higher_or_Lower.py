#!/usr/bin/env python


#We are playing the Guess Game. The game is as follows:
#I pick a number from 1 to n. You have to guess which number I picked.
#Every time you guess wrong, I'll tell you whether the number is higher or lower.
#You call a pre-defined API guess(int num) which returns 3 possible results (-1, 1, or 0):

#-1 : My number is lower
# 1 : My number is higher
# 0 : Congrats! You got it!


# THERE IS A CORNER CASE DEPENDING ON WHETHER YOU ARE USING floor or ceiling!!!
from math import floor

class Solution(object):
    def set_expected_value(self, value):
        self.value = value

    def guess(self, num):
        if num == self.value:
            return 0
        if num < self.value:
            return -1
        if num > self.value:
            return 1

    def guessNumber(self, n):
        """
        :type n: int
        :rtype: int
        """
        start = 0
        end = n
        while True:
          h = floor((end - start)/2.0 + start)
          ret = self.guess(h)
          print("start %d, end %d, hypothesis %d" % (start, end, h))
          if ret == 0:
              print("Bingo, the num is %d" % h)
              return h
          elif ret == -1:
              if start == h:
                  start = h + 1
              else:
                  start = h
          elif ret == 1:
              if end == h:
                  end = h - 1
              else:
                  end = h


if __name__ == '__main__':
    print("choose 6 from 0 - 10")
    sol = Solution()
    sol.set_expected_value(6)
    sol.guessNumber(10)

    print("choose 23 from 0 - 100")
    sol = Solution()
    sol.set_expected_value(23)
    sol.guessNumber(100)

    print("choose 1 from 0 - 1")
    sol = Solution()
    sol.set_expected_value(1)
    sol.guessNumber(1)

    print("choose 0 from 0 - 1")
    sol = Solution()
    sol.set_expected_value(0)
    sol.guessNumber(1)
