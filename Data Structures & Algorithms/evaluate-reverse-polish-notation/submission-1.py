class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []

        for item in tokens:
            if item in '+*-/':
                a = int(stack.pop())
                b = int(stack.pop())
                res = None
                match item:
                    case '+':
                        res = a+b
                    case '*':
                        res = a*b
                    case '/':
                        res = b/a
                    case '-':
                        res = b-a
                stack.append(res)

            else:
                stack.append(item)
        
        return int(stack.pop())