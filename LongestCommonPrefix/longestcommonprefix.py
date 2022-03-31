"""
14. Longest Common Prefix

Write a function to find the longest common prefix string amongst an array of strings.
If there is no common prefix, return an empty string "".

Example 1:
========================================================================
Input: strs = ["flower","flow","flight"]
Output: "fl"

Example 2:
========================================================================
Input: strs = ["dog","racecar","car"]
Output: ""

Explanation: There is no common prefix among the input strings.
"""
from typing import List


class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        answer = ""

        min_length = min([len(x) for x in strs])
        if min_length == 0:
            return answer

        for i in range(0, min_length):
            if any(str_[i] != strs[0][i] for str_ in strs):
                break

            answer += strs[0][i]

        return answer

