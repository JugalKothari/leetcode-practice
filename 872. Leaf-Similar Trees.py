# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def leafSimilar(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> bool:
        def dfs(root,ls):
            if not root:
                return
            if not root.left and not root.right:
                ls.append(root.val)
            dfs(root.left,ls)
            dfs(root.right,ls)
        l1,l2=[],[]
        dfs(root1,l1)
        dfs(root2,l2)
        return l1==l2
        
