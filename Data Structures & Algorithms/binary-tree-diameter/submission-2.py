# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        """
        recursive again. with base case not affecting result.
        as i go through each node recursively, how can I keep
        track of height? Each layer means an additional increment
        but not just that. it is dependent on both the left
        and right nodes
        """
        dia = 0

        def dfs(curr):
            if not curr:
                return 0
            
            left = dfs(curr.left)
            right = dfs(curr.right)
            nonlocal dia
            dia = max(dia, left + right)
            return 1 + max(left, right)

        dfs(root)
        return dia

