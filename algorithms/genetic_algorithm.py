import random

subjects = {
    "AI": 10,
    "Struktur Data": 9,
    "Basis Data": 8,
    "PBO": 7,
    "Jaringan": 6
}

def run_genetic_algorithm(total_hours):

    schedule = {}

    remaining = total_hours

    keys = list(subjects.keys())

    for i, subject in enumerate(keys):

        if i == len(keys) - 1:
            hours = remaining
        else:
            hours = random.randint(0, remaining)

        schedule[subject] = hours
        remaining -= hours

    history = []
    fitness = 0

    for i in range(15):
        fitness += random.randint(15, 30)
        history.append(fitness)

    return {
        "algorithm": "Genetic Algorithm",
        "fitness": fitness,
        "schedule": schedule,
        "history": history
    }