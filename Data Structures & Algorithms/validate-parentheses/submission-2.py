class Solution:
    def isValid(self, s: str) -> bool:

        stack = []

        for c in s:
            if self.isOpening(c):
                stack.append(c)
            else:

                if len(stack) == 0:
                    return False
                opening = stack.pop()
               
                if not self.isCorrect(opening, c):
                    return False
                
        return len(stack) == 0
    
    def isOpening(self, c):
        return c == '(' or c=='[' or c=='{'


    def isCorrect(self, opening, closing):
        return opening + closing == "()" or opening + closing == "[]" or opening + closing == "{}"
            
        