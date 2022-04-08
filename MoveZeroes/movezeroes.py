"""
283. Move Zeroes

Given an integer array nums, move all 0's to the end of it while maintaining the relative order of the non-zero elements.

Note that you must do this in-place without making a copy of the array.



Example 1:
========================================================================
Input: nums = [0,1,0,3,12]
Output: [1,3,12,0,0]

Example 2:
========================================================================
Input: nums = [0]
Output: [0]
"""

from typing import List


class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        last_nonzero_found_at = 0

        for i in range(len(nums)):
            if nums[i] != 0:
                nums[last_nonzero_found_at] = nums[i]
                last_nonzero_found_at += 1

        for i in range(last_nonzero_found_at, len(nums)):
            nums[i] = 0


if __name__ == '__main__':
    nums = [0, 1, 0, 3, 12]
    Solution().moveZeroes(nums)
    print(nums)
