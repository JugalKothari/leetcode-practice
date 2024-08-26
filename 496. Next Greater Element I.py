#Faster solution
class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        hashmap={}
        stack=[]

        for i in reversed(nums2):
            while stack and stack[-1]<=i:
                stack.pop()
            hashmap[i]=stack[-1] if stack else -1
            stack.append(i)
        
        return [hashmap[num] for num in nums1]

#My solution
class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        answers=[]
        for i in range(len(nums1)):
            idx=nums2.index(nums1[i])
            for j in range(idx+1, len(nums2)):
                if nums2[j]>nums2[idx]:
                    answers.append(nums2[j])
                    break
            if len(answers)<i+1:
                answers.append(-1)
        return answers       
