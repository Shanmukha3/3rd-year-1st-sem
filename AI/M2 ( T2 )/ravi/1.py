def resolution(knowledge_base, goal):
    clauses = knowledge_base + [goal]

    while True:
        new_clauses = []
        for i in range(len(clauses)):
            for j in range(i + 1, len(clauses)):
                resolvents = set(clauses[i]) | set(clauses[j])
                for literal in resolvents.copy():
                    if ("not", literal) in resolvents or (literal[0] == "not" and literal[1] in resolvents):
                        resolvents.remove(("not", literal))
                        resolvents.remove(literal)
                if not resolvents:
                    return True  # Goal reached
                new_clauses.append(tuple(resolvents))

        if all(new_clause in clauses or new_clause in new_clauses for new_clause in new_clauses):
            return False  # No new resolvents found, cannot reach the goal

        clauses += new_clauses

# Knowledge base for the puzzle
knowledge_base = [
    ("Box", "A"),
    ("Box", "B"),
    ("Box", "C"),
    ("Color", "Red"),
    ("Color", "Blue"),
    ("Color", "Green"),
    ("HasBall", "A", "Red"),
    ("HasBall", "B", "Blue"),
    ("HasBall", "C", "Green"),
]

# Goal: Select a ball such that if it's red, then we win
goal = [
    ("HasBall", "x", "Red"),
]

# Check if there is a solution to the puzzle
result = resolution(knowledge_base, goal)

if result:
    print("You win! Select a red ball.")
else:
    print("No solution found.")