n = 3
jobs = [5, 2, 6, 1, 4]

def s(n, jobs):
    machines = [0] * n

    jobs.sort(reverse=True)

    for j in jobs:
        lowest_workload = min(machines)
        m = machines.index(lowest_workload)

        machines[m] += j

    return max(machines)


print(s(n, jobs))