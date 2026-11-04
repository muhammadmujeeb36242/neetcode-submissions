# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        length = 1
        if root.left or root.right:
            if not root.left:
                length += self.maxDepth(root.right)
            elif not root.right:
                length += self.maxDepth(root.left)
            else:
                length += max(self.maxDepth(root.left), self.maxDepth(root.right))
        return length
            