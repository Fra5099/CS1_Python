
"""
File: store_location.py
Assignment: lab 06
Language: python3
Author: Faisal Alzahrany
Purpose: finding the best location for store by median distance strategy
CSCI 141
"""

import time as tm

def readfile(filename):
    """
    this function read the text file and put the elements in a list
    :param filename: the file text name
    :return:
    """
    file=open(filename)
    num=1
    list=[]
    for ch in file:
        ch=ch.split()
        count=0
        x=""
        y=""
        while len(ch)>count:
            if ch[count].isdigit()==True:
                y=ch[count:]
                break
            elif ch[count]==" ":
                pass
            else:
                x+=ch[count]
            count+=1
        y=int(y[0])
        insideList=[[x,y]]
        list+=insideList
    return list

def quick_sort( L ):# the edition one for this program
    """
    quickSort: List( A ) -> List( A )
        where A is 'totally ordered'
    """
    if L == []:
        return []
    else:
        pivot = L[0]
        ( less, same, more ) = partition( pivot, L )
        return quick_sort( less ) + same + quick_sort( more )

def partition( pivot, L ):# the edition one for this program
    """
    partition: A * List( A ) -> Tuple( List( A ), List( A ), List( A ) )
        where A is totally ordered
    """
    ( less, same, more ) = ( [], [], [] )
    pivot=pivot[1]
    for e in L:
        num=e[1]
        if num < pivot:
            less.append( e )
        elif num > pivot:
            more.append( e )
        else:
            same.append( e )
    return ( less, same, more )


def median(lst):
    """
    this function find the best location by using median strategy
    :param lst: the list of locations
    :return:
    """
    new_list=quick_sort(lst)
    m=len(new_list)
    if m%2==0:
        a=new_list[m//2]
        b=new_list[(m//2)-1]
        return (a[1]+b[1])/2
    else:
        b=new_list[m//2]
        return b[1]

def distance(lst,loc):
    """
    this function sum's the distances to the best location
    :param lst: the list of locations
    :param loc: the best location
    :return:
    """
    dis=0
    for i in range(0,len(lst)):
        i=lst[i]
        if i[1]>=loc:
            dis+=(i[1]-loc)
        else:
            dis+=(loc-i[1])
    return dis

def main():

    filename=input("Enter data file: ")
    lst=readfile(filename)
    start = tm.time()
    b=median(lst)
    print("Optimum new store location: ",b)
    end = tm.time()
    print("Sum of distances to new store: ",distance(lst,b))

    print("elapsed time: ",end-start)

main()