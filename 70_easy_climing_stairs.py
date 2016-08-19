#!/usr/bin/env python


# You are climbing a stair case. It takes n steps to reach to the top.
#
# Each time you can either climb 1 or 2 steps. In how many distinct ways can you climb to the top?

# Analysis
# Recursion:
# if n=1, f(n=1) = 1
# if n=2, first step takes 1 or first step takes 2, f(2) = 1 + 1 = 2
# if n=3, f(3) = f(2) + f(1)
# f(n) = f(n-1) + f(n-2)
#
# Non-recursion

class Solution(object):
    def climbStairs2(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n == 1:
            return 1
        if n == 2:
            return 2

        return self.climbStairs(n-1) + self.climbStairs(n-2)


    def climbStairs(self, n):
        if n == 1:
            return 1
        if n == 2:
            return 2

        dp = [0] * (n+1)
        dp[0] = 1  # virtual
        dp[1] = 1
        for x in range(2, n+1):    # 2,3,...,n
          dp[x] = dp[x-1] + dp[x-2]

        return dp[n]
