class Solution:
    def partition(self, s: str) -> List[List[str]]:
        partitions=[]
        def check_palindrome(substr):
            return substr==substr[::-1]
        def solve(s, partition):
            if s=="":
                partitions.append(partition[:])
                return
            for i in range(len(s)):
                substr=s[:i+1]
                if check_palindrome(substr):
                    partition.append(substr)
                    solve(s[i+1:], partition)
                    partition.pop()
                else:
                    continue

        solve(s, [])
        return partitions
