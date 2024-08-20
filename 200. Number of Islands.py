class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        visited=[[False]*len(grid[0]) for i in range(len(grid))]
        def dfs(i,j):
            visited[i][j]=True
            del_row=[-1,0,1,0]
            del_col=[0,1,0,-1]
            for k in range(4):
                new_row=i+del_row[k]
                new_col=j+del_col[k]
                if new_row>=0 and new_row<len(grid) and new_col>=0 and new_col<len(grid[0]):
                    if not visited[new_row][new_col] and grid[new_row][new_col]=="1":
                        dfs(new_row, new_col)
        
        islands=0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if not visited[i][j] and grid[i][j]=="1":
                    dfs(i,j)
                    islands+=1
        
        return islands
