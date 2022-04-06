"""
File: select_median.py
Assignment: lab 06
Language: python3
Author: Faisal Alzahrany
Purpose: finding the best location for store by quick select
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



def quick_select(aList,k):
    """
    this function find's the k^th smallest number
    :param aList: list of elements
    :param k: the k^th smallest number
    :return:
    """
    if len(aList)!=0:
        pivot=aList[len(aList)//2]
        smallerList=[]
        largerList=[]
        count=0
        for i in aList:

            if i[1]==pivot[1]:
                count+=1
            if i[1]>pivot[1]:
                largerList+=[i]
            if i[1]<pivot[1]:
                smallerList+=[i]

        m=len(smallerList)
        if k>=m and k<m+count:
            return pivot[1]
        if m>k:
            return quick_select(smallerList,k)
        else:
            return quick_select(largerList,k-m-count)

def best_loc(lst):
    """
    this function find the best location by using quick select
    :param lst: the list of locations
    :return:
    """
    m=len(lst)
    if m%2==0:
        a=quick_select(lst,m//2)
        b=quick_select(lst,(m//2)-1)
        return (a+b)/2
    else:
        b=lst[m//2]
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
    b=best_loc(lst)
    print("Optimum new store location: ",b)
    end = tm.time()
    print("Sum of distances to new store: ",distance(lst,b))

    print("elapsed time: ",end-start)

main()