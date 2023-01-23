class Solution:
    def evalRPN(self, tokens: List[str]) -> int:

        if len(tokens) < 2:
            return int(tokens[0])

        stack = []
        rpn = deque(tokens)
        stack.append(int(rpn.popleft()))
        stack.append(int(rpn.popleft()))

        while len(rpn) > 0:
            current = rpn.popleft()
            if current == "+":
                a = stack.pop()
                b = stack.pop()
                stack.append(a+b)
            elif current == "-":
                a = stack.pop()
                b = stack.pop()
                stack.append(b-a)
            elif current == "*":
                a = stack.pop()
                b = stack.pop()
                stack.append(a*b)
            elif current == "/":
                a = stack.pop()
                b = stack.pop()
                stack.append(int(b/a))
            else:
                stack.append(int(current))

        return stack[0]
