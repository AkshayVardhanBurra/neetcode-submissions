class Solution:
    def evalRPN(self, tokens: List[str]) -> int:

        stack = []

        for token in tokens:
            if self.isNumber(token):
                print(f"adding {token}")
                stack.append(int(token))
            else:
                num1 = stack.pop()
                num2 = stack.pop()

                result = int(self.computeOperation(num2, num1, token))
                stack.append(result)

        return stack.pop()

            

    
    def isNumber(self, char):
        try:
            char = int(char)
            return True
        except:
            return False

    def computeOperation(self, num1, num2, op):
        if op == "+":
            return num1 + num2
        elif op == "-":
            return num1 - num2
        elif op == "/":
            return int(num1 / num2)
        elif op == "*":
            return num1 * num2
        else:
            print(f"here! {op}")
            return 0