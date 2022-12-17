# leetcode 150. Evaluate Reverse Polish Notation

class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = list()
        for i in tokens :
            if i == "+" :
                a = stack.pop()
                b = stack.pop()
                stack.append(b+a)
            elif i == "-" :
                a = stack.pop()
                b = stack.pop()
                stack.append(b-a)
            elif i == "*" :
                a = stack.pop()
                b = stack.pop()
                stack.append(b*a)
            elif i == "/" :
                a = stack.pop()
                b = stack.pop()
                stack.append(int(float(b)/a))
            else :
                stack.append(int(i))
        return stack[0]