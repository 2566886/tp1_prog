def tokenize(expression: str) -> list[str]:
    conversion = list(expression)
    for i in conversion:
        if i == ' ':
            conversion.remove(i)
    return conversion

#def infix_to_postfix(tokens: list[str]) -> list[str]:

#def evaluate_postfix(tokens: list[str]) -> float:

a = "3 + 4 * 2 / ( 1 - 5 )"
tokens = tokenize(a)
print(tokens)