def job_sequencing(jobs):
    jobs.sort(key=lambda x: x[2], reverse=True)

    n = len(jobs)
    slot = [False] * n
    result = ['-1'] * n

    for job in jobs:
        for j in range(min(n, job[1])-1, -1, -1):
            if not slot[j]:
                slot[j] = True
                result[j] = job[0]
                break

    print("Selected Jobs:", result)


jobs = [
    ('A', 2, 100),
    ('B', 1, 19),
    ('C', 2, 27),
    ('D', 1, 25),
    ('E', 3, 15)
]

job_sequencing(jobs)