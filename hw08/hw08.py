"""
File: HW08.py
Author: Faisal Alzahrany
"""

import random
import time as tm
from merge_sort import *
from quick_sort import *
from insertion_sort import *

def get_list1(n):
    """
    :param n: the length of a list
    :return: a list with random elements (favorable to quick sort)
    """
    L = []
    for i in range(n):
        L = L+[random.random()]
    return L

def get_list2(n):
    """
    :param n: the length of a list
    :return: a list with many repeated elements (favorable to quick sort)
    """
    L = []
    for i in range(n):
        L = L+[random.randint(1,100)]
    return L


def get_list3(n):
    """
    Expected behavior of quick sort: poor
    :param n: the length of a list
    :return: a list of elements increasing overall
    (unfavorable to quick sort)
    """
    L = []
    for i in range(n):
        L = L + [random.random()*i]
    return L

def get_list4(n):
    """
    :param n: the length of a list
    :return: a list with many zeros but neither increasing nor decreasing
    (unfavorable to quick sort)
    """
    L = []
    for i in range(n):
        L = L + [random.randint(-8, 8)*i]
    return L


def merge_quick_sort(lst):
    """
    this function sort the list by mixed algorithm between merge sort and quick sort
    :param lst: a list
    :return:
    """
    if lst==[]:
        return []
    elif len(lst)==1:
        return lst
    else:
        x,y=split(lst)
        x1,x2,x3=partition(x[0],x)
        y1,y2,y3=partition(y[0],y)
        return merge(merge_quick_sort(x1)+x2+merge_quick_sort(x3),merge_quick_sort(y1)+y2+merge_quick_sort(y3))


def test_merge_quick_sort():
    """
    this function test merge quick sort
    :return:
    """
    print("Testing the correctness of merge_quick_sort:")
    lst=get_list2(8)
    print("Before sorted:")
    print(lst)
    print("After sorted:")
    a_list=merge_quick_sort(lst)
    print(a_list)


def test_list1():
    """
    this function compare the elapsed time between all the sort algorithms by using list 1
    :return:
    """
    print("Testing with list 1")
    list1_i=get_list1(1000)
    list1_m=get_list1(1000)
    list1_q=get_list1(1000)
    list1_qm=get_list1(1000)
    start=tm.time()
    insertion_sort(list1_i)
    end=tm.time()
    print("insertion_sort elapsed time: ",end-start,"seconds")
    start=tm.time()
    merge_sort(list1_m)
    end=tm.time()
    print("merge_sort elapsed time:",end-start,"seconds")
    start=tm.time()
    merge_quick_sort(list1_qm)
    end=tm.time()
    print("merge_quick_sort elapsed time:",end-start,"seconds")
    start=tm.time()
    quick_sort(list1_q)
    end=tm.time()
    print("quick_sort elapsed time:",end-start,"seconds")


def test_list2():
    """
    this function compare the elapsed time between all the sort algorithms by using list 2
    :return:
    """
    print("Testing with list 2")
    list_i=get_list2(1000)
    list_m=get_list2(1000)
    list_q=get_list2(1000)
    list_qm=get_list2(1000)
    start=tm.time()
    insertion_sort(list_i)
    end=tm.time()
    print("insertion_sort elapsed time: ",end-start,"seconds")
    start=tm.time()
    merge_sort(list_m)
    end=tm.time()
    print("merge_sort elapsed time:",end-start,"seconds")
    start=tm.time()
    merge_quick_sort(list_qm)
    end=tm.time()
    print("merge_quick_sort elapsed time:",end-start,"seconds")
    start=tm.time()
    quick_sort(list_q)
    end=tm.time()
    print("quick_sort elapsed time:",end-start,"seconds")


def test_list3():
    """
    this function compare the elapsed time between all the sort algorithms by using list 3
    :return:
    """
    print("Testing with list 3")
    list_i=get_list3(1000)
    list_m=get_list3(1000)
    list_q=get_list3(1000)
    list_qm=get_list3(1000)
    start=tm.time()
    insertion_sort(list_i)
    end=tm.time()
    print("insertion_sort elapsed time: ",end-start,"seconds")
    start=tm.time()
    merge_sort(list_m)
    end=tm.time()
    print("merge_sort elapsed time:",end-start,"seconds")
    start=tm.time()
    merge_quick_sort(list_qm)
    end=tm.time()
    print("merge_quick_sort elapsed time:",end-start,"seconds")
    start=tm.time()
    quick_sort(list_q)
    end=tm.time()
    print("quick_sort elapsed time:",end-start,"seconds")

def test_list4():
    """
    this function compare the elapsed time between all the sort algorithms by using list 4
    :return:
    """
    print("Testing with list 4")
    list_i=get_list4(1000)
    list_m=get_list4(1000)
    list_q=get_list4(1000)
    list_qm=get_list4(1000)
    start=tm.time()
    insertion_sort(list_i)
    end=tm.time()
    print("insertion_sort elapsed time: ",end-start,"seconds")
    start=tm.time()
    merge_sort(list_m)
    end=tm.time()
    print("merge_sort elapsed time:",end-start,"seconds")
    start=tm.time()
    merge_quick_sort(list_qm)
    end=tm.time()
    print("merge_quick_sort elapsed time:",end-start,"seconds")
    start=tm.time()
    quick_sort(list_q)
    end=tm.time()
    print("quick_sort elapsed time:",end-start,"seconds")

def test_compare():
    """
    this function prints all the previous tests
    :return:
    """
    test_list1()
    print("")
    test_list2()
    print("")
    test_list3()
    print("")
    test_list4()
    print("")
    print("Time comparison test ends.")

def main():
    test_merge_quick_sort()
    print("")
    test_compare()


main()