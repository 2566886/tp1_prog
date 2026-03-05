from shunting_yard import tokenize, infix_to_postfix, evaluate_postfix

class ParanthesesError(ValueError):
    """Paranthèses non appariées."""
    pass

class NombreError(ValueError):
    """Nombre mal formé."""
    pass

class OpérateurError(ValueError):
    """Opérateur inconnu."""
    pass

def gestion_parantheses(expression: str) -> bool:
    if expression.count('(') != expression.count(')'):
        raise ParanthesesError("Le nombre de paranthèses ouvrantes ne correspond pas au nombre de paranthèses fermantes.")
    return True
    
def gestion_nombre(expression: str) -> bool:
    for token in tokenize(expression):
        if token not in ['+', '-', '*', '/', '(', ')']:
            try:
                float(token)
            except ValueError:
                raise NombreError(f"Le token '{token}' n'est pas un nombre valide.")
    return True

def gestion_opérateur(expression: str) -> bool:
    for token in tokenize(expression):
        if token not in ['+', '-', '*', '/', '(', ')'] and gestion_nombre(expression) == False:
            try:
                float(token)
            except ValueError:
                raise OpérateurError(f"L'opérateur '{token}' n'est pas valide.")
    return True

def gestion_denominateur_zero(expression: str) -> bool:
    for token in tokenize(expression):
        if token == '/' and tokenize(expression)[tokenize(expression).index(token) + 1] == '0':
            raise ZeroDivisionError("Division par zéro détectée.")
    return True

def gestion_expression_invalide(expression: str) -> bool:
    for token in tokenize(expression):
        if token in ['+', '-', '*', '/', '(', ')'] and tokenize(expression)[tokenize(expression).index(token)] in ['+', '-', '*', '/', '(', ')'] and tokenize(expression)[tokenize(expression).index(token) + 1] in ['+', '-', '*', '/', '(', ')']:
            raise IndexError("Vérifiez la syntaxe de votre expression.")
    return True


