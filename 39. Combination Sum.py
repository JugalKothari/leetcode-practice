class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        combinations=[]
        def solve(target: int, subseq: list, start:int):
            if target==0:
                combinations.append(subseq[:])
                return
            for i in range(start, len(candidates)):
                num=candidates[i]
                if target-num>=0:
                    subseq.append(num)
                    solve(target-num, subseq, i)
                    subseq.pop()
            
        solve(target, [], 0)
        return combinations
                
