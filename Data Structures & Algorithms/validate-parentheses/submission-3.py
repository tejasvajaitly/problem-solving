class Solution:
    def isValid(self, s: str) -> bool:
        myStack = []
        s = list(s)

        for i in range(len(s) - 1, -1, -1):
            bracket = s.pop()
            if len(myStack) == 0:
                myStack.append(bracket)
            elif bracket == '(' and myStack[-1] == ')':
                myStack.pop()
            elif bracket == '[' and myStack[-1] == ']':
                myStack.pop()
            elif bracket == '{' and myStack[-1] == '}':
                myStack.pop()
            else:
                myStack.append(bracket)
        
        if len(myStack) == 0:
            return True
        else:
            return False



#create a new stack
#pop from the original and push into the stack only if its closing
#pop for the original and pop from the stack if its a matching opening
#the stack should be empty for us to return true
        