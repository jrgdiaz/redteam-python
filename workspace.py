from concurrent.futures import ThreadPoolExecutor

def run_io_tasks_in_parallel(tasks,max_workers):
    with ThreadPoolExecutor(max_workers=max_workers) as executor: 
        running_tasks = [executor.submit(task) for task in tasks]
        for running_task in running_tasks:
            running_task.result()

"""
run_io_tasks_in_parallel([
    lambda: print('IO task 1 running!'),
    lambda: print('IO task 2 running!'),
])
"""

