class Solution:
    def trap(self, height: List[int]) -> int:
        i=0
        j=len(height)-1
        left_max = height[i]
        right_max = height[j]
        sum=0
        while i<j:
            if left_max<=right_max:
                sum+=left_max-height[i]
                i+=1
                left_max = max(height[i],left_max)
            else:
                sum+=right_max - height[j]
                j-=1
                right_max = max(right_max, height[j])
        return sum
