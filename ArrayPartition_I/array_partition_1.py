"""
Given an integer array nums of 2n integers,
group these integers into n pairs (a1, b1), (a2, b2), ..., (an, bn)
such that the sum of min(ai, bi) for all i is maximized. Return the maximized sum.

Example 1:
========================================================================
Input: nums = [1,4,3,2]
Output: 4

Example 2:
========================================================================
Input: nums = [6,2,6,5,1,2]
Output: 9

"""
from typing import List


class Solution:
    def arrayPairSum(self, nums: List[int]) -> int:
        return sum(sorted(nums)[::2])


if __name__ == "__main__":
    print(Solution().arrayPairSum([1, 4, 3, 2]))
