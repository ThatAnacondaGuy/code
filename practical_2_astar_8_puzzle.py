import heapq

goal = (1, 2, 3, 4, 5, 6, 7, 8, 0)


def heuristic(state):
    distance = 0

    for i in range(9):
        if state[i] != 0:
            goal_pos = state[i] - 1

            x1, y1 = i // 3, i % 3
            x2, y2 = goal_pos // 3, goal_pos % 3

            distance += abs(x1 - x2) + abs(y1 - y2)

    return distance


def get_neighbors(state):
    neighbors = []
    zero = state.index(0)

    row = zero // 3
    col = zero % 3

    moves = [(-1, 0), (1, 0), (0, -1), (0, 1)]

    for dr, dc in moves:
        r = row + dr
        c = col + dc

        if 0 <= r < 3 and 0 <= c < 3:
            new_pos = r * 3 + c
            new_state = list(state)

            new_state[zero], new_state[new_pos] = (
                new_state[new_pos], new_state[zero]
            )

            neighbors.append(tuple(new_state))

    return neighbors


def astar(start):
    priority_queue = [(heuristic(start), 0, start)]

    parent = {start: None}
    cost = {start: 0}

    while priority_queue:
        f, g, current = heapq.heappop(priority_queue)

        if current == goal:
            path = []

            while current is not None:
                path.append(current)
                current = parent[current]

            return path[::-1]

        if g != cost[current]:
            continue

        for neighbor in get_neighbors(current):
            new_cost = g + 1

            if neighbor not in cost or new_cost < cost[neighbor]:
                cost[neighbor] = new_cost
                parent[neighbor] = current

                new_f = new_cost + heuristic(neighbor)
                heapq.heappush(
                    priority_queue, (new_f, new_cost, neighbor)
                )

    return None


start = (1, 2, 3, 4, 0, 6, 7, 5, 8)
solution = astar(start)

if solution:
    print("Solution Found!")

    for state in solution:
        for i in range(0, 9, 3):
            print(state[i:i + 3])
        print()

    print("Total Moves:", len(solution) - 1)
else:
    print("No Solution Found")
