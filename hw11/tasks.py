"""
file: tasks.py
author: Faisal Alzahrany
description: homework
"""

from dataclasses import *
from priority_queue import *

@dataclass
class Task:
    name: str
    priority: int

def make_task(name,priority):
    return Task(name,priority)


def test_tasks():
    q = make_priority_queue()
    enqueue(q, make_task("Task1", 5))
    enqueue(q, make_task("Task2", 7))
    enqueue(q,make_task("Task3",1))
    enqueue(q,make_task("Task4",9))
    t = front(q)
    print("Highest priority task is", t.name, "with priority",
          t.priority)
    t = back(q)
    print("Lowest priority task is", t.name, "with priority",
          t.priority)
    while not is_empty(q):
        t = front(q)
        dequeue(q)

def main():
    test_tasks()

main()