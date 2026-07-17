# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        """looks like another problem where I can solve
        it recursively so I'll give that a try. So the
        base case will be to check if the root is null
        if it is, we want that to not affect the sum we
        finally return so it should be set to 0. We need
        some sort of way to have each call receive the
        information from the recursion, so we should be
        returning a cumulative value up the stack.
        """
        if not root:
            return 0
        depth = 1 + max(self.maxDepth(root.right), self.maxDepth(root.left))
        print(depth)
        return depth
