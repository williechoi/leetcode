"""
344. Reverse String
Write a function that reverses a string. The input string is given as an array of characters s.
You must do this by modifying the input array in-place with O(1) extra memory.



Example 1:
========================================================================
Input: s = ["h","e","l","l","o"]
Output: ["o","l","l","e","h"]

Example 2:
========================================================================
Input: s = ["H","a","n","n","a","h"]
Output: ["h","a","n","n","a","H"]
"""
from typing import List


class Solution:
    def reverseString(self, strs: List[str]) -> None:
        left_index, right_index = 0, len(strs) - 1
        while left_index < right_index:
            strs[left_index], strs[right_index] = strs[right_index], strs[left_index]
            left_index += 1
            right_index -= 1


if __name__ == '__main__':
    list1 = ['h', 'e', 'l', 'l', 'o']
    list2 = ["H", "a", "n", "n", "a", "h"]
    Solution().reverseString(list1)
    Solution().reverseString(list2)
    assert list1 == ['o', 'l', 'l', 'e', 'h']
    assert list2 == ["h", "a", "n", "n", "a", "H"]
