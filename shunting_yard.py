def tokenize(expression: str) -> list[str]:
    conversion = list(expression)
    for i in conversion:
        if i == ' ':
            conversion.remove(i)
    return conversion

def infix_to_postfix(tokens: list[str]) -> list[str]:
    precedence = {'+': 2, '-': 2, '*': 3, '/': 3, '(': 0, ')': 0}
    output = []
    stack = []
    for token in tokens:
        if token not in precedence:
            output.append(token)
        elif token == '(':
            stack.insert(0, token)
        elif token == ')':
            while stack[0] != '(':
                output.append(stack.pop(0))
            stack.pop(0)
        else:
            if stack != []:
                if precedence[token] > precedence[stack[0]]:
                    stack.insert(0, token)
                elif precedence[token] < precedence[stack[0]]:
                    stack.append(token)
                elif precedence[token] == precedence[stack[0]]:
                    output.append(stack.pop(0))
                    stack.insert(0, token)
            else:
                stack.append(token)
    output.extend(stack)
    return output
            

def evaluate_postfix(tokens: list[str]) -> float:
    stack = []
    for token in tokens:
        if token not in ['+', '-', '*', '/']:
            stack.append(float(token))
        else:
            deuxieme_terme = stack.pop()
            premier_terme = stack.pop()
            if token == '+':
                stack.append(premier_terme + deuxieme_terme)
            elif token == '-':
                stack.append(premier_terme - deuxieme_terme)
            elif token == '*':
                stack.append(premier_terme * deuxieme_terme)
            elif token == '/':
                stack.append(premier_terme / deuxieme_terme)
    return stack[0]
