import random

from timeitpoj.timeit import TimeIt

BASE_TIME = 0.01


# Function to simulate some computational task
def compute_task():
    amount = random.randint(1000, 5000)
    for i in range(amount):
        result = i * 2


execution_map = {
    "task 1": {
        "count": 5,
        "children": {
            "task 1.1": {
                "count": 3,
                "children": {
                    "task 1.1.1": {
                        "count": 2,
                        "children": {}
                    },
                    "task 1.1.2": {
                        "count": 2,
                        "children": {}
                    }
                }
            }
        }
    },
    "task 2": {
        "count": 5,
        "children": {
            "task 2.1": {
                "count": 3,
                "children": {
                    "task 2.1.1": {
                        "count": 2,
                        "children": {}
                    },
                    "task 2.1.2": {
                        "count": 2,
                        "children": {}
                    },
                    "task 2.1.3": {
                        "count": 2,
                        "children": {}
                    }
                },
            },

            "task 2.2": {
                "count": 3,
                "children": {
                    "task 2.2.1": {
                        "count": 9,
                        "children": {}
                    },
                    "task 2.2.2": {
                        "count": 1,
                        "children": {}
                    },
                    "task 2.2.3": {
                        "count": 2,
                        "children": {}
                    }
                },
            }
        }
    }
}

with TimeIt("my simple timer") as timer1:
    compute_task()
with TimeIt("my timer") as timer:
    def execute_task(task_name, task_count, children):
        for _ in range(task_count):
            with timer(task_name):
                compute_task()
                for child_name, child in children.items():
                    execute_task(child_name, child["count"], child["children"])


    for task_name, task in execution_map.items():
        execute_task(task_name, task["count"], task["children"])
