# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> int:
        ticks=defaultdict(int)
        ticks[0]=1
        def dfs(root,total):
            count=0
            if root:
                total=total+root.val
                count=ticks[total-targetSum]
                ticks[total]+=1
                print(count)
                count+=dfs(root.left,total)+dfs(root.right,total)
                ticks[total]-=1
            return count
        return dfs(root,0)
