class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        endindex=len(nums1)-1
        while n>0 and m>0:
            if nums1[m-1]<nums2[n-1]:
                nums1[endindex]=nums2[n-1]
                endindex-=1
                n-=1
            else:
                nums1[endindex]=nums1[m-1]
                m-=1
                endindex-=1
        if n:
            while n>0:
                nums1[endindex]=nums2[n-1]
                n-=1
                endindex-=1
        else:
            while m>0:
                nums1[endindex]=nums1[m-1]
                m-=1
                endindex-=1
              
