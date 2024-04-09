class Solution:
    def decodeString(self, s: str) -> str:
        stack=[]
        curr_num=0
        curr_str=''
        for ch in s:
            if ch.isdigit():
                curr_num=curr_num*10+int(ch)
            elif ch=='[':
                stack.append(curr_num)
                stack.append(curr_str)
                curr_num=0
                curr_str=''
            elif ch==']':
                prev_str=stack.pop()
                prev_num=stack.pop()
                curr_str=prev_str + curr_str*prev_num
            else:
                curr_str+=ch
        while stack:
            curr_str=stack.pop()+curr_str
        return curr_str
