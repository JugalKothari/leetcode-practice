# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxLevelSum(self, root: Optional[TreeNode]) -> int:
        maxLevel=1
        maxsum=float('-inf')
        queue=deque()
        queue.append(root)
        level=0
        while queue:
            levelsum=0
            queuesize=len(queue)
            for levelnode in range(queuesize):
                currnode=queue.popleft()
                levelsum+=currnode.val
                if currnode.left:
                    queue.append(currnode.left)
                if currnode.right:
                    queue.append(currnode.right)
            level+=1
            if levelsum>maxsum:
                maxlevel=level
                maxsum=levelsum
        return maxlevel
