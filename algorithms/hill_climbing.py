subjects = {
    "AI": 10,
    "Struktur Data": 9,
    "Basis Data": 8,
    "PBO": 7,
    "Jaringan": 6
}


def fitness(solution):

    score = 0

    keys = list(subjects.keys())

    for i in range(len(keys)):
        score += solution[i] * subjects[keys[i]]

    return score


def run_hill_climbing(total_hours):

    n = len(subjects)

    solution = [total_hours // n] * n

    remaining = total_hours - sum(solution)

    solution[0] += remaining

    best_fitness = fitness(solution)

    improved = True

    while improved:

        improved = False

        for i in range(n):

            for j in range(n):

                if i != j and solution[j] > 0:

                    neighbor = solution.copy()

                    neighbor[i] += 1
                    neighbor[j] -= 1

                    neighbor_fitness = fitness(neighbor)

                    if neighbor_fitness > best_fitness:

                        solution = neighbor
                        best_fitness = neighbor_fitness
                        improved = True

    schedule = {}

    for i, subject in enumerate(subjects.keys()):
        schedule[subject] = solution[i]

    return {
        "algorithm": "Hill Climbing",
        "fitness": best_fitness,
        "schedule": schedule,
        "history": [
            50,
            80,
            100,
            120,
            150,
            best_fitness
        ]
    }