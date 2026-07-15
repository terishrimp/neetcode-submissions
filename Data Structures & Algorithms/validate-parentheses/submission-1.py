class Solution:
    def isValid(self, s: str) -> bool:
        #initialize stack
        stack = []
        #define dictionary mapping closed brackets to open
        closedToOpen = {"}":"{", "]":"[", ")":"("}
        #go through string
        for c in s:
        #if the character maps to open brackets
            if c in closedToOpen:
                #we check if the stack still has any more elements
                #if it does and the stack's top matches to the dict value
                if stack and closedToOpen[c] == stack[-1]:
                    #we remove it and move to the next
                    stack.pop()
                else:
                    return False
            else:
                #otherwise we add it to the stack since it's an opening bracket
                stack.append(c)
        return True if not stack else False
            

