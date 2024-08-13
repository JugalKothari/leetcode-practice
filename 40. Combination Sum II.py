class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        self.res=[]
        candidates.sort()
        self.dfs(candidates, target, 0, [])
        return self.res

    def dfs(self, candidates, target, index, path):
        if target==0:
            self.res.append(path[:])
            return
        if target<0:
            return
        
        for i in range(index, len(candidates)):
            if i>index and candidates[i]==candidates[i-1]:
                continue
            path.append(candidates[i])
            self.dfs(candidates, target-candidates[i], i+1, path)
            path.pop()
