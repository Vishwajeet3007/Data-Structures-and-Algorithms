def fcfs_disk_scheduling(requests, start):
    total_head_movement = 0
    current_head_position = start

    for request in requests:
        total_head_movement += abs(request - current_head_position)
        current_head_position = request

    return total_head_movement

if __name__ == "__main__":
    # Example usage
    requests = [98, 183, 37, 122, 14, 124, 65, 67]  # Example disk access requests
    initial_head_position = 53  # Initial head position

    total_movement = fcfs_disk_scheduling(requests, initial_head_position)
    print(f"Total head movement using FCFS: {total_movement}")
