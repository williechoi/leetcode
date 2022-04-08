"""
22. Generate Parentheses
Given n pairs of parentheses, write a function to generate all combinations of well-formed parentheses.

Example 1:
========================================================================
Input: n = 3
Output: ["((()))","(()())","(())()","()(())","()()()"]

Example 2:
========================================================================
Input: n = 1
Output: ["()"]
"""


from typing import List


class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        if n == 1:
            return ["()"]
        elif n == 2:
            return ["(())", "()()"]
        else:
            answer = self.generateParenthesis(n-1)
            new_answer = [*answer]
            return new_answer


if __name__ == '__main__':
    print(Solution().generateParenthesis(5))










