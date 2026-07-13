# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        self.ans=0
        def heightM(root):
            if not root:
                return 0
            lh=heightM(root.left)
            rh=heightM(root.right)
            self.ans=max(self.ans,lh+rh)
            return 1+max(lh,rh)
        heightM(root)
        return self.ans
