#!/usr/bin/env python

# Given two arrays, write a function to compute their intersection.
#
# Example:
#
# Given nums1 = [1, 2, 2, 1], nums2 = [2, 2], return [2].
#
# Note:
#
# Each element in the result must be unique.
# The result can be in any order.


class Solution(object):
    @classmethod
    def intersection(cls, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        return list(set(nums1).intersection(set(nums2)))


if __name__ == "__main__":
    print(Solution.intersection([1,2,2,1], [2,2]))


# HashMap unordered_map can give O(N) Solution
#         vector<int> ans;
#         unordered_map<int, int> hashmap;
#         for (auto i : nums1) {
#             hashmap[i] = 1;
#         }
#         for (auto i : nums2) {
#             if (hashmap.find(i) != hashmap.end()) {
#                 ans.push_back(i)
#             }
#         }
