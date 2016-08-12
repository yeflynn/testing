#!/usr/bin/env python

# Shuffle a set of numbers without duplicates.
#
# Example:
#
# // Init an array with set 1, 2, and 3.
# int[] nums = {1,2,3};
# Solution solution = new Solution(nums);
#
# // Shuffle the array [1,2,3] and return its result. Any permutation of [1,2,3] must equally likely to be returned.
# solution.shuffle();
#
# // Resets the array back to its original configuration [1,2,3].
# solution.reset();
#
# // Returns the random shuffling of array [1,2,3].
# solution.shuffle();


# Permutation  P^k_n = n! / (n-k)!
# Combination  C^k_n = P^k_n / k!
#

import random
class Solution(object):
    def __init__(self, nums):
        """
        :type nums: List[int]
        :type size: int
        """
        self.base = nums

    def reset(self):
        return self.base

    def randIndex(self):
        return random.randint(0, len(self.base)-1)

    def shuffle(self):
        """
        shuffle the nums list/array
        """
        # use randint to generate random index
        nums = []
        index_list = []
        while True:
            if len(index_list) == len(self.base):
                break
            index = self.randIndex()
            if index not in index_list:
                index_list.append(index)

        for x in index_list:
            nums.append(self.base[x])
        return nums

if __name__ == '__main__':
    print("Expect 4! permutations for a list of 4")
    sol = Solution([1,2,3,4])
    permutations = set()
    for trial in xrange(1000):
        permutations.add(str(sol.shuffle()))

    print(len(permutations))
    print(permutations)
