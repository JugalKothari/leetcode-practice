#User function Template for python3

class Solution:
    def kthElement(self, k, arr1, arr2):
        A, B = arr1, arr2
        total = len(A) + len(B)
        if len(A)>len(B):
            A, B = B, A
        l=max(0, k-len(B))
        r=min(len(A)-1, k)
        while True:
            i=(l+r)//2
            j=k-i-2
            
            
            Aleft=A[i] if i>=0 else float('-inf')
            Aright=A[i+1] if i+1<len(A) else float('inf')
            Bleft=B[j] if j>=0 else float('-inf')
            Bright=B[j+1] if j+1<len(B) else float('inf')
            
            if Aleft<=Bright and Bleft<=Aright:
                return max(Aleft,Bleft)
                
            elif Aleft>Bright:
                r=i-1
            else:
                l=i+1
