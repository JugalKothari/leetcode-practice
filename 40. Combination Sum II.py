class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        combinations=[]
        candidates.sort()
        def solve(target, subseq, index):
            if target==0:
                combinations.append(subseq[:])
                return
            for i in range(index, len(candidates)):
                if i>index and candidates[i-1]==candidates[i]:
                    continue
                if candidates[i]>target:
                    break
                candidate=candidates[i]
                if target-candidate>=0:
                    subseq.append(candidate)
                    solve(target-candidate, subseq, i+1)
                    subseq.pop()
        solve(target, [], 0)
        return combinations
            
