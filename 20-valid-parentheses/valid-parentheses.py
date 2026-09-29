class Solution:
    def isValid(self, s: str) -> bool:
        stack=[]
        for ch in s:
            if ch=='(' or ch=='{' or ch=='[':
                stack.append(ch)
            else:
                if not stack:
                    return False
            
            if ch==')':
                if stack[-1]!='(':
                    return False 
                
                stack.pop()
            if ch == '}':
                if stack[-1] != '{':
                    return False
                stack.pop()
        
            if ch == ']':
                if stack[-1] != '[':
                    return False
                stack.pop()

        return not stack