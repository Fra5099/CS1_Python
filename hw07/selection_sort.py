"""
File: selection_sort.py
Assignment: hw
Language: python3
Author: Faisal Alzahrany
Purpose: sorting any list by using selection sort
CSCI 141
"""

"""
1- when the list is already sorted the insertion sort performing is better than selection sort

2- selection sort performing in this case is worse because selection sort scan every element
while the insertion sort will not scan anything in that case because it's already sorted
"""



def readfile(filename):
    """
    this function read the text file and convert it to list
    :param filename: file name
    :return:
    """
    file=open(filename)
    new_list=[]
    for i in file:
        num=int(i)
        new_list+=[num]
    return new_list

def find_min_from(lst,mark):
    """
    this function find the minimum number inside a list with specific range
    :param lst: the list that is going to be searched in it
    :param mark:  a mark in which range in the list to search
    :return: the index of the minimum number
    """
    newlist=lst[mark:]
    min=newlist[0]
    index=0
    for i in range(0,len(newlist)):
        if newlist[i]<min:
            min=newlist[i]
            index=i
    return index+mark

def swap( lst, i, j ):
    """
    swap: List NatNum NatNum -> None
    swap the contents of list at pos i and j.
    Parameters:
        lst - the list of data
        i   - index of one datum
        j   - index of the other datum
    """
    temp = lst[i]
    lst[i] = lst[j]
    lst[j] = temp

def selection_sort(lst):
    """
    this function sort the list by finding the minimum number
    :param lst: the list that is going to be sorted
    :return: the sorted list
    """
    for mark in range(0,len(lst)):
        swap(lst,mark,find_min_from(lst,mark))
    return lst


def main():
    filename=input("Enter the file name: ")
    lst=readfile(filename)
    print(lst)
    selection_sort(lst)
    print(lst)


main()