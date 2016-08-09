#!/usr/bin/env python


# You are playing the following Nim Game with your friend:
#There is a heap of stones on the table, each time one of you take turns to remove 1 to 3 stones.
#The one who removes the last stone will be the winner. You will take the first turn to remove the stones.

# Both of you are very clever and have optimal strategies for the game.
# Write a function to determine whether you can win the game given the number of stones in the heap.

# For example, if there are 4 stones in the heap, then you will never win the game:
#no matter 1, 2, or 3 stones you remove, the last stone will always be removed by your friend.


# Recursion is too slow when n is large
class Solution2(object):
    def canWinNim(self, n):
        """
        :type n: int
        :rtype: bool
        """
        if n <= 3:
            return True

        # can my peer win if I take 1 or 2 or 3?
        return not (self.canWinNim(n-1) and self.canWinNim(n-2) and self.canWinNim(n-3))

class Solution(object):
    def canWinNim(self, n):
        """
        :type n: int
        :rtype: bool
        """
        # If i leave 1,2,3, I lose
        # if i leave 4, I win.
        # leave 5,6,7 I lose
        # leave 8, I win
        if (n % 4) in [1,2,3]:
            return True
        else:
            return False


if __name__ == "__main__":
    solution = Solution()
    for n in xrange(30):
        print("start with %d stones, can I win? %d" % (n, solution.canWinNim(n)))
