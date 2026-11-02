cities = ["A", "B", "C", "D", "E"]

dist = [
    [0, 10, 15, 20, 25],
    [10, 0, 35, 25, 30],
    [15, 35, 0, 30, 20],
    [20, 25, 30, 0, 15],
    [25, 30, 20, 15, 0]
]


def distance(route):
    total = 0

    for i in range(len(route)):
        a = cities.index(route[i])
        b = cities.index(route[(i + 1) % len(route)])
        total += dist[a][b]

    return total


def neighbors(route):
    result = []

    for i in range(len(route)):
        for j in range(i + 1, len(route)):
            new_route = list(route)
            new_route[i], new_route[j] = new_route[j], new_route[i]
            result.append(tuple(new_route))

    return result


def beam_search():
    beam = [
        tuple("ABCDE"),
        tuple("ACBDE"),
        tuple("ADBCE")
    ]

    k = 3

    while True:
        candidates = set(beam)

        for route in beam:
            candidates.update(neighbors(route))

        new_beam = sorted(candidates, key=distance)[:k]

        if new_beam == beam:
            break

        beam = new_beam

    best = min(beam, key=distance)
    return best, distance(best)


route, cost = beam_search()

print("Best Route:", " -> ".join(route + (route[0],)))
print("Minimum Distance:", cost)
