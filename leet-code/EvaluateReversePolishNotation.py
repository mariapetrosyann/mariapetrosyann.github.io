class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        for token in tokens:
            if token not in '+-*/':
                stack.append(int(token))
            else:
                right_number = stack.pop()
                left_number = stack.pop()
                match token:
                    case '+':
                        stack.append(left_number + right_number)
                    case '-':
                        stack.append(left_number - right_number)
                    case '*':
                        stack.append(left_number * right_number)
                    case '/':
                        stack.append(int(left_number / right_number))
        return stack.pop()
