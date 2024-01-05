# Define predicates
def Parent(x, y): return ("Parent", x, y)
def Male(x): return ("Male", x)
def Female(x): return ("Female", x)
def Brother(x, y): return ("Brother", x, y)

# Define the knowledge base
knowledge_base = [
    Parent("John", "Susan"),
    Male("John"),
    Parent("Susan", "Mary"),
    Female("Susan"),
    Parent("Mary", "Tom"),
]

# Define the negation of the goal (John is Susan's uncle)
goal_negation = [
    ("not", Brother("a", "b")),
    Male("a"),
    Parent("a", "Susan"),
    Female("b"),
]

# Perform resolution
def resolve(clause1, clause2):
    resolved_clause = set(clause1) | set(clause2)
    for literal in resolved_clause:
        if ("not", literal) in resolved_clause or (literal[0] == "not" and literal[1] in resolved_clause):
            resolved_clause.remove(("not", literal))
            resolved_clause.remove(literal)
    return tuple(resolved_clause)

def is_goal_reached(clause, goal_negation):
    return all(literal in clause or ("not", literal) in clause for literal in goal_negation)

def resolution(knowledge_base, goal_negation):
    clauses = knowledge_base + [goal_negation]

    while True:
        new_clauses = []
        for i in range(len(clauses)):
            for j in range(i + 1, len(clauses)):
                resolvents = resolve(clauses[i], clauses[j])
                if not resolvents:
                    return True  # Goal reached
                new_clauses.append(resolvents)

        if all(new_clause in clauses or new_clause in new_clauses for new_clause in new_clauses):
            return False  # No new resolvents found, cannot reach the goal

        clauses += new_clauses

# Check if John is Susan's uncle
result = resolution(knowledge_base, goal_negation)

if result:
    print("John is Susan's uncle.")
else:
    print("John is not Susan's uncle.")