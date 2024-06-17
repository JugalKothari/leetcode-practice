# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        def dfs(root: TreeNode, maxnum: int, count: int) -> int:
            if not root:
                return count
            if root.val>=maxnum:
                maxnum=root.val
                count+=1
            count = dfs(root.left, maxnum, count)
            count = dfs(root.right, maxnum, count)
            return count
        return dfs(root, root.val, 0)
