from sympy import symbols, Or, Not, satisfiable

# Define symbols
A, B, C = symbols('A B C')
Red, Green, Blue = symbols('Red Green Blue')

# Define the knowledge base
knowledge_base = [
    Or(Red(A), Not(Green(A))),  # Rule 1
    Or(Green(B), Not(Blue(B))),  # Rule 2
    Or(Blue(A), Blue(B), Blue(C)),  # Rule 3
]

# Check if the puzzle is solvable
model = satisfiable(knowledge_base)

if model:
    print("The puzzle is solvable.")
    print("Solution:")
    for symbol in model:
        print(f"{symbol}: {model[symbol]}")
else:
    print("The puzzle is unsolvable.")