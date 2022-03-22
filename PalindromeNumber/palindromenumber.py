"""
9. Palindrome Number

Given an integer x, return true if x is palindrome integer.
An integer is a palindrome when it reads the same backward as forward.
- for example, 121 is a palindrome while 123 is not.

Example 1:
========================================================================
Input: x = 121
Output: true
Explanation: 121 reads as 121 from left to right and from right to left.

Example 2:
========================================================================
Input: x = -121
Output: false
Explanation: From left to right, it reads -121. From right to left, it becomes 121-.
Therefore it is not a palindrome.

Example 3:
========================================================================
Input: x = 10
Output: false
Explanation: Reads 01 from right to left.
Therefore it is not a palindrome.
"""


class Solution:
    def isPalindrome(self, x: int) -> bool:
        strx = str(x)
        return self.isPalindrome2(strx)

    def isPalindrome2(self, x: str):
        if len(x) == 1:
            return True
        elif len(x) == 2:
            return x[0] == x[1]
        else:
            if x[0] != x[len(x) - 1]:
                return False

            return self.isPalindrome2(x[1:len(x) - 1])


if __name__ == '__main__':
    solution = Solution()
    print(solution.isPalindrome(121))