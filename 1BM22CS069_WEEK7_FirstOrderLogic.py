def unify(x, y):
    """
    Unifies two terms x and y.
    Returns the Most General Unifier (MGU) or raises a UnificationError if unification fails.
    """
    substitutions = {}  # θ: Initial empty substitution set
    stack = [(x, y)]  # Pairs to unify

    while stack:
        a, b = stack.pop()

        if a == b:
            continue  # No unification needed for identical terms

        elif is_variable(a):
            substitutions = unify_variable(a, b, substitutions)

        elif is_variable(b):
            substitutions = unify_variable(b, a, substitutions)

        elif is_compound(a) and is_compound(b):
            if function_name(a) != function_name(b) or arity(a) != arity(b):
                raise UnificationError(f"Cannot unify {a} and {b} - Function mismatch")
            stack.extend(zip(arguments(a), arguments(b)))  # Add argument pairs to the stack

        else:
            raise UnificationError(f"Cannot unify {a} and {b} - Term mismatch")

    return substitutions


def unify_variable(var, term, substitutions):
    """
    Handles unification when one of the terms is a variable.
    """
    if var in substitutions:
        return unify(substitute(var, substitutions), substitute(term, substitutions))

    elif term in substitutions:
        return unify(substitute(var, substitutions), substitute(term, substitutions))

    elif occurs_check(var, term, substitutions):
        raise UnificationError(f"Occurs check failed: {var} occurs in {term}")

    else:
        substitutions[var] = term
        return substitutions


def substitute(term, substitutions):
    """
    Applies the substitutions to a term.
    """
    while is_variable(term) and term in substitutions:
        term = substitutions[term]
    if is_compound(term):
        return (function_name(term), [substitute(arg, substitutions) for arg in arguments(term)])
    return term


def occurs_check(var, term, substitutions):
    """
    Checks if var occurs in term, directly or indirectly, to prevent infinite loops.
    """
    if var == term:
        return True
    elif is_compound(term):
        return any(occurs_check(var, arg, substitutions) for arg in arguments(term))
    return False


# Utility Functions for Term Handling
def is_variable(term):
    return isinstance(term, str) and term.islower()  # Lowercase strings represent variables


def is_compound(term):
    return isinstance(term, tuple) and len(term) > 1  # Compound terms are tuples


def function_name(term):
    return term[0] if is_compound(term) else None  # The first element of a compound term is its function name


def arguments(term):
    return term[1:] if is_compound(term) else []  # The rest of the tuple contains arguments


def arity(term):
    return len(arguments(term))  # Number of arguments in a compound term


# Exception Class for Errors
class UnificationError(Exception):
    pass


# Example Usage
if __name__ == "__main__":
    # Example: Unify P(f(x), y) with P(f(a), b)
    term1 = ("P", ("f", "x"), "y")
    term2 = ("P", ("f", "a"), "b")

    try:
        result = unify(term1, term2)
        print("Unification successful! Substitutions:", result)
    except UnificationError as e:
        print("Unification failed:", e)
