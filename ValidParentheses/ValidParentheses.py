"""
20. Valid Parentheses
Given a string s containing just the characters '(', ')', '{', '}', '[' and ']',
determine if the input string is valid.

An input string is valid if:

Open brackets must be closed by the same type of brackets.
Open brackets must be closed in the correct order.

Example 1:
========================================================================
Input: s = "()"
Output: true

Example 2:
========================================================================
Input: s = "()[]{}"
Output: true

Example 3:
========================================================================
Input: s = "(]"
Output: false
"""


class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        for char in s:
            if char in ('(', '{', '['):
                stack.append(char)
            else:
                if not stack:
                    return False
                elif char == ')' and stack.pop() != '(':
                    return False
                elif char == '}' and stack.pop() != '{':
                    return False
                elif char == ']' and stack.pop() != '[':
                    return False

        return True if not stack else False
