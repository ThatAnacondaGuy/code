def get_next_states(state):
    a, b = state
    states = []

    # Fill the jugs
    states.append((4, b))
    states.append((a, 3))

    # Empty the jugs
    states.append((0, b))
    states.append((a, 0))

    # Pour water from 4L jug into 3L jug
    transfer = min(a, 3 - b)
    states.append((a - transfer, b + transfer))

    # Pour water from 3L jug into 4L jug
    transfer = min(b, 4 - a)
    states.append((a + transfer, b - transfer))

    return states


def dfs():
    stack = [(0, 0)]
    visited = {(0, 0)}

    while stack:
        current = stack.pop()
        a, b = current

        if a == 2 or b == 2:
            return current

        for next_state in get_next_states(current):
            if next_state not in visited:
                visited.add(next_state)
                stack.append(next_state)

    return None


solution = dfs()

if solution:
    print("Solution Found!")
    print("Final State:", solution)
else:
    print("No Solution Found")
