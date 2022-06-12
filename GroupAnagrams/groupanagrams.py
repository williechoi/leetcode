"""
49. Group Anagrams
Given an array of strings strs, group the anagrams together. You can return the answer in any order.

An Anagram is a word or phrase formed by rearranging the letters of a different word or phrase,
typically using all the original letters exactly once.

Example 1:
========================================================================
Input: strs = ["eat","tea","tan","ate","nat","bat"]
Output: [
    ["bat"],
    ["nat","tan"],
    ["ate","eat","tea"]
]

Example 2:
========================================================================
Input: strs = [""]
Output: [
    [""]
]

Example 3:
========================================================================
Input: strs = ["a"]
Output: [
    ["a"]
]
"""

from typing import List
import collections


class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagrams = collections.defaultdict(list)
        for word in strs:
            anagrams[''.join(sorted(word))].append(word)

        return list(anagrams.values())


if __name__ == "__main__":
    print(Solution().groupAnagrams(["eat", "tea", "tan", "ate", "nat", "bat"]))
