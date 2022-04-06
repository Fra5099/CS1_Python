"""
Faisal Alzahrany

CSCI 141
"""


def print_sequence_rec(start,count):
    """
    recursively generates and prints count steps
    of the sequence from the start value.
    :param start: start value
    :param count: how many sequence
    :return:
    """
    if count<1:
        print(start)
    elif start==0:
        return 0
    else:
        print(start,end=" ")
        print_sequence_rec((start*2)+5,count-1)



def print_sequence_iter(start, count):
    """
    iteratively generates and prints count steps
    of the double and add 5 sequence from the start value
    :param start: start value
    :param count:
    :return:
    """

    while True:
        i = start
        start=(start*2)+5
        print(i,end=" ")
        count-=1
        if count <0:
            break


def find_end_rec(start,count):
    """
    recursively finds and returns the last value in the
    sequence that begins with start and ends after count steps.
    :param start: start value
    :param count: how many steps
    :return:
    """
    if count<1:
        return start
    elif start==0:
        return 0
    else:
        return find_end_rec((start*2)+5,count-1)


def find_end_iter(start, count):
    """
    iteratively finds and returns the last value in
    the sequence that begins with start and ends after count steps.
    :param start: start value
    :param count: how many steps
    :return:
    """
    while True:
        if count <1:
            break
        start=(start*2)+5
        count-=1
    return start


def find_start_rec(goal,count,start=0):
    """
    recursively searches forward from an initial value
    of 0, and returns the smallest integer value that reaches or exceeds the goal.
    :param goal: the number is wanted to be exceed
    :param count: how many steps in the sequence
    :param start: intitial value or start value
    :return:
    """
    if goal<0:
        pass
    elif count<1:
        pass
    else:
        x=find_end_rec(start,count)
        if x ==goal or x>goal:
            return start
        else:
            return find_start_rec(goal,count,start+1)



def find_start_itr(goal,count):
    """
    iteratively searches forward from an initial value
    of 0, and returns the smallest integer value that reaches or exceeds the goal.
    :param goal: the number is wanted to be exceed
    :param count: how many steps in the sequence
    :return:
    """
    if goal < 0:
        pass
    elif count < 1:
        pass
    else:
        start=0
        while True:

            x=find_end_iter(start,count)
            if x>=goal:
                break
            start=start+1
        return start


def test_double_add_5():
    """
    function tests all the previous functions
    :return:
    """
    print_sequence_rec(1,2)
    print_sequence_iter(1,2)
    print("")
    print_sequence_rec(3,3)
    print("")
    print_sequence_iter(3,3)
    print("")
    print(find_end_rec(100,3))
    print(find_end_iter(100,3))
    print(find_end_rec(40,2))
    print(find_end_iter(40,2))
    print(find_start_rec(100,1))
    print(find_start_itr(100,1))
    print(find_start_rec(150,4))
    print(find_start_itr(150,4))

def main():
    test_double_add_5()


main()

