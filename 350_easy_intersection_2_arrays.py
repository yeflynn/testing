#!/usr/bin/env python

#Given two arrays, write a function to compute their intersection.

#Example:
#Given nums1 = [1, 2, 2, 1], nums2 = [2, 2], return [2, 2].

#Note:

#Each element in the result should appear as many times as it shows in both arrays.
#The result can be in any order.
#Follow up:

#What if the given array is already sorted? How would you optimize your algorithm?
#What if nums1's size is small compared to num2's size? Which algorithm is better?
#What if elements of nums2 are stored on disk, and the memory is limited such that you cannot load all elements into the memory at once?

# Question: data size, sorted or not, where is data
# Complexity is O(m*n)
class Solution(object):
    @classmethod
    def intersect(cls, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        intersect = []
        for m in nums1:
            if nums2.count(m) > 0:
                intersect.append(m)
                nums2.remove(m)
        return intersect


    # Complexity:
    #  sorting O(nlogn) + O(mlogm)
    #  find intersection:  1/k * O(mn)
    @classmethod
    def intersectSorted(cls, nums1, nums2):
        # check nums1 is sorted
        # check nums2 is sorted
        intersect = []
        for m in nums1:
            print("test value %d" % m)
            index = cls.findFirstIndex(nums2, m)
            print("index in nums2 %d" % index)
            if index >= 0:
                intersect.append(m)
                nums2 = nums2[index+1:]  # assume there is a magic low overhead operation.
        return intersect

    @classmethod
    def findFirstIndex(cls, nums, val):
        """
        nums: a sorted list, asc
        val: val to be found
        ret: first index for val, -1 if not found
        """
        for index in range(len(nums)):
            if nums[index] == val:
                return index
            elif nums[index] > val:
                return -1
        return -1


    # Complexity:
    #  Get count unique numbers HyperLogLog

    @classmethod
    def intersectCountersForBigData(cls, nums1, nums2):
        intersect = []
        cu2 = collections.Counter(nums2)   # Counter object
        cu1 = collections.Counter(nums1)

        for key in cu1.iterkeys():
            if cu2.has_key(key):
                min_count = min(cu1.get(key), cu2.get(key))
                intersect.append([key]*min_count)

        return intersect




# if nums1 and nums2 sizes are very imbalanced. Direct join might be better.

# Counter can be added across machines
# if nums2 is too large to fit into memory -> counters
#   load chunk K of nums2 into memory
#   Get unique counters {value: distince count}
#   Combine counters with previous counter
# problem solved.


# This is overkill
# if nums2 is too large to fit into memory -> sth like MR
#   load nums2 into K mappers
#   assume nums1 has L distinct values, then we have L reducers
#   mappers shard the input data by value
#   reducer gets {value, unique count} for nums2
# We can also get {value, unique count} for nums1
# problem solved.



if __name__ == '__main__':
    print("find intersection of [1,2,2,1] and [1,1,2,3]")
    ret = Solution.intersect([1,2,2,1], [1,1,2,3])
    print(str(ret))

    print("find intersection of [1,1,2,4] and [1,2,4,4,5]")
    ret = Solution.intersectSorted([1,1,2,4], [1,2,4,4,5])
    print(str(ret))

    print("find intersection of [1,1,2,4] and [1,2,4,4,5]")
    import collections
    ret = Solution.intersectCountersForBigData([1,2,3,4] * 100, [1,2,2,3,3,3,4,4,4,4])
    print(str(ret))
