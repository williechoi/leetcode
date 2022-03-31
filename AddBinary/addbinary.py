"""
67. Add Binary

Given two binary strings a and b, return their sum as a binary string.

Find two lines that together with the x-axis form a container, such that the container contains the most water.
Return the maximum amount of water a container can store.
Notice that you may not slant the container.

Example 1:
========================================================================
Input: a = "11", b = "1"
Output: "100"

Example 2:
========================================================================
Input: a = "1010", b = "1011"
Output: "10101"


Constraints:
========================================================================
- 1 <= a.length, b.length <= 104
- a and b consist only of '0' or '1' characters.
- Each string does not contain leading zeros except for the zero itself.
"""


class Solution:
    def addBinary(self, a: str, b: str) -> str:
        decimal_a = self.calcDecimalSum(a)
        decimal_b = self.calcDecimalSum(b)

        return str(bin(decimal_a + decimal_b))[2:]

    def calcDecimalSum(self, bin_str: str):
        intsum = 0
        for i, ch in enumerate(bin_str):
            if ch == '0':
                continue

            intsum += 2**(len(bin_str) - i - 1)

        return intsum









print(Solution().addBinary("1010", "1011"))