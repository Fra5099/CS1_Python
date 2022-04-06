"""
file: priority_queue.py
author: Faisal Alzahrany
description: homework
"""
from node import Node
from dataclasses import dataclass
from typing import Union


@dataclass
class PriorityQueue:
    size: int
    front: Union[None, Node]
    back: Union[None, Node]


def make_priority_queue():
    """
    Returns a new queue with size initialized to zero and
    the front and back fields initialized to the empty sequence.
    """
    return PriorityQueue(0, None, None)

def enqueue(queue,element):
    """
    this function insert the element in the priority queue depending in the element priority
    """
    newnode = Node(element, None)
    if is_empty(queue):
        queue.front = newnode
        queue.size = queue.size + 1
        queue.back = newnode

    else:
        index=priority_index(queue,element.priority)
        queue.front=insert_at_front(index,element,queue.front)
        queue.size+=1
        if element.priority<queue.back.value.priority:
            queue.back.value=element

def insert_at_front(index, element, lnk):
    """
    this function insert the element in the front node in the queue
    """
    if index == 0:
        return Node(element, lnk)
    elif lnk != None:
        return Node(lnk.value, insert_at_front(index-1, element, lnk.rest))
    else:
        raise IndexError("index out of bounds in insert_at")


def priority_index(queue,priority):
    """
    this function return the right priority index to insert the element inside the priority queue
    :param queue:
    :param priority:  integer priority from the element
    :return: index
    """
    index=0
    count=queue.front
    while count is not None:
        if priority>=count.value.priority:
            break
        count=count.rest
        index+=1
    return index



def dequeue(queue):
    """
    Remove the front element from the queue. (returns removed value)
    precondition: queue is not empty.
    """
    if is_empty(queue):
        raise IndexError("dequeue on empty queue")
    removed = queue.front.value
    queue.front = queue.front.rest
    if is_empty(queue):
        queue.back = None
    queue.size = queue.size - 1
    return removed

def front(queue):
    """
    Access and return the first element in the queue without removing it.
    precondition: queue is not empty.
    """
    if is_empty(queue):
        raise IndexError("front on empty queue")
    return queue.front.value

def back(queue):
    """
    Access and return the last element in the queue without removing it
    precondition: queue is not empty.
    """
    if is_empty(queue):
        raise IndexError("back on empty queue")
    return queue.back.value

def is_empty(queue):
    """
    Is the queue empty?
    """
    return queue.front == None

