import heapq
import time

class JobScheduler:
    def __init__(self):
        self.job_queue = []

    def add_job(self, job, priority):
        heapq.heappush(self.job_queue, (priority, time.time(), job))

    def execute_job(self):
        if self.job_queue:
            priority, _, job = heapq.heappop(self.job_queue)
            print(f"Executing job: {job} with priority {priority}")
        else:
            print("No jobs to execute.")

# Example usage
scheduler = JobScheduler()

scheduler.add_job("Task 1", 3)
scheduler.add_job("Task 2", 1)
scheduler.add_job("Task 3", 2)

scheduler.execute_job()  # Executes the job with the highest priority
scheduler.execute_job()
scheduler.execute_job()
scheduler.execute_job()  # No jobs to execute
