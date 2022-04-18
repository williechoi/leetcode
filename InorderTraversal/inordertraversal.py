"""
94. Binary Tree Inorder Traversal
Given the root of a binary tree, return the inorder traversal of its nodes' values.


Example 1:
==============================================================================
Input: root = [1,null,2,3]
Output: [1,3,2]

Example 2:
========================================================================
Input: root = []
Output: []

Example 3:
========================================================================
Input: root = [1]
Output: [1]
"""

from typing import Optional, List


class TreeNode:
    # Definition for a binary tree node.
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        if root is None or root.val is None:
            return []

        answer = []
        answer += self.inorderTraversal(root.left)
        answer.append(root.val)
        answer += self.inorderTraversal(root.right)

        return answer

