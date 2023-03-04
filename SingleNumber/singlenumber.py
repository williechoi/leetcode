"""
136. Single Number

Given a non-empty array of integers nums, every element appears twice except for one. Find that single one.
You must implement a solution with a linear runtime complexity and use only constant extra space.



Example 1:
========================================================================
Input: nums = [2,2,1]
Output: 1

Example 2:
========================================================================
Input: nums = [4,1,2,1,2]
Output: 4

Example 3:
========================================================================
Input: nums = [1]
Output: 1
"""

from typing import List


class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        xor = nums[0]
        for i in range(1, len(nums)):
            xor ^= nums[i]

        return xor


if __name__ == "__main__":
    example1 = [2, 2, 2, 2, 4, 4, 5, 5, 3, 3, 3, 7, 7, 7, 7]
    example2 = [4, 1, 2, 1, 2]
    print(Solution().singleNumber(example1))    # 3
    print(Solution().singleNumber(example2))    # 4

