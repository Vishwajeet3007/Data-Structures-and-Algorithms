def is_safe_state(processes, available, max_matrix, allocation):
    num_processes = len(processes)
    num_resources = len(available)

    need = [[0] * num_resources for _ in range(num_processes)]
    for i in range(num_processes):
        for j in range(num_resources):
            need[i][j] = max_matrix[i][j] - allocation[i][j]

    work = available[:]
    finish = [False] * num_processes
    safe_sequence = []

    while len(safe_sequence) < num_processes:
        found = False
        for i in range(num_processes):
            if not finish[i]:
                if all(need[i][j] <= work[j] for j in range(num_resources)):
                    for j in range(num_resources):
                        work[j] += allocation[i][j]
                    safe_sequence.append(i)
                    finish[i] = True
                    found = True
                    break
        if not found:
            return False, []

    return True, safe_sequence

def main():
    processes = [0, 1, 2, 3, 4]
    available = [3, 3, 2]
    max_matrix = [
        [7, 5, 3],
        [3, 2, 2],
        [9, 0, 2],
        [2, 2, 2],
        [4, 3, 3]
    ]
    allocation = [
        [0, 1, 0],
        [2, 0, 0],
        [3, 0, 2],
        [2, 1, 1],
        [0, 0, 2]
    ]

    is_safe, safe_sequence = is_safe_state(processes, available, max_matrix, allocation)

    if is_safe:
        print("The system is in a safe state.")
        print("Safe sequence:", safe_sequence)
    else:
        print("The system is not in a safe state.")

if __name__ == "__main__":
    main()
