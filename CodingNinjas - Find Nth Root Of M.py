def NthRoot(n: int, m: int) -> int:
    low=1
    high=m

    while low<=high:
        mid=(low+high)//2

        if mid**n>m:
            high=mid-1
            continue
        elif mid**n==m:
            return mid
        else:
            low=mid+1
    return -1
  
