# timing.py

import time

class ExecutionTimer:
    def __init__(self, repetitions=1):
        self.repetitions = repetitions

    def __call__(self, func):
        def timer(*args, **kwargs):
            result = None
            total_time = 0
            print(f"Running {func.__name__}() {self.repetitions} times")
            for _ in range(self.repetitions):
                start = time.perf_counter()
                result = func(*args, **kwargs)
                end = time.perf_counter()
                total_time += end - start
            average_time = total_time / self.repetitions
            print(
                f"{func.__name__}() takes "
                f"{average_time * 1000:.4f} ms on average"
            )
            return result

        return timer
    
@ExecutionTimer(repetitions=100)
def square_numbers(numbers):
    return [number ** 2 for number in numbers]


square_numbers(list(range(100)))  

