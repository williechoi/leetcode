"""
461. Hamming distance.
The Hamming distance between two integers is the number of positions at which the corresponding bits are different.
Given two integers x and y, return the Hamming distance between them.

Example 1:
==============================================================================
Input: x = 1, y = 4
Output: 2

Explanation:
1   (0 0 0 1)
4   (0 1 0 0)
       ↑   ↑
The above arrows point to positions where the corresponding bits are different.

Example 2:
==============================================================================
Input: x = 3, y = 1
Output: 1

Constraints:
0 <= x, y <= 2^31 - 1
"""


class Solution:
    def hammingDistance(self, x: int, y: int) -> int:
        return bin(x ^ y).count('1')


if __name__ == "__main__":
    example1 = (4, 5)   # 0100 0101 -> 1
    example2 = (7, 8)   # 0111 1000 -> 4
    example3 = (15, 4)  # 1111 0100 -> 3
    print(Solution().hammingDistance(example1[0], example1[1]))
    print(Solution().hammingDistance(example2[0], example2[1]))
    print(Solution().hammingDistance(example3[0], example3[1]))
