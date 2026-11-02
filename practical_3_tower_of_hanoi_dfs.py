def get_next_states(state):
    states = []

    for i in range(3):
        if state[i]:
            disk = state[i][-1]

            for j in range(3):
                if i != j:
                    if not state[j] or state[j][-1] > disk:
                        new_state = [list(peg) for peg in state]

                        new_state[i].pop()
                        new_state[j].append(disk)

                        states.append(
                            tuple(tuple(peg) for peg in new_state)
                        )

    return states


def dfs():
    start = ((3, 2, 1), (), ())
    goal = ((), (), (3, 2, 1))

    stack = [(start, [start])]
    visited = {start}

    while stack:
        current, path = stack.pop()

        if current == goal:
            return path

        for next_state in get_next_states(current):
            if next_state not in visited:
                visited.add(next_state)
                stack.append((next_state, path + [next_state]))

    return None


solution = dfs()

if solution:
    print("Solution Found!")

    for step, state in enumerate(solution):
        print("Step", step, ":", state)

    print("Total Moves:", len(solution) - 1)
else:
    print("No Solution Found")
