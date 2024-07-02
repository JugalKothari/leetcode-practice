# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return []
        self.rightpov=[]
        def bfs(root, level):
            if root:
                if len(self.rightpov) == level:
                    self.rightpov.append(root.val)
                bfs(root.right, level + 1)
                bfs(root.left, level + 1)
            return
        bfs(root, 0)
        return self.rightpov
        
