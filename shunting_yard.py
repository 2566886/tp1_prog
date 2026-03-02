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
            

#def evaluate_postfix(tokens: list[str]) -> float:

a = "3 + 4 * 2 / ( 1 - 5 )"
b = []
c = infix_to_postfix(tokenize(a))
b.insert(4, 'a')
b.append('b')
b.insert(0, 'c')
#print(b)
tokens = tokenize(a)
#print(type(tokens[0]))
#print(tokens[0])
print(c)
