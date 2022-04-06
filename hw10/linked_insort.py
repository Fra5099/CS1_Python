"""
file: linked_insort.py
author: Faisal Alzahrany
description: homework
"""

from linked_code import *

def insert( value, lnk ):

    """
    Put the value in the proper spot in the linked list to keep it sorted.
    New nodes are created.
    :param value: the value to add to the sequence of values in the list
    :param lnk: the node at the head of the list
    :return: a (partially) new linked list with the value inserted
    :pre: the list headed by lnk is sorted.
    :post: the link returned refers to a list that is sorted.
    """
    if lnk is None:
        return LinkNode(value,None)
    elif lnk.rest is None:
        return LinkNode(lnk.value,LinkNode(value,None))
    elif lnk.value<=value<=lnk.rest.value:
        return LinkNode(lnk.value,LinkNode(value,lnk.rest))
    else:
        return LinkNode(lnk.value,insert(value,lnk.rest))

def insort( lnk ):
    """
    Return a copy of a linked list where all the values are sorted,
    with the lowest value at the head.
    :param lnk: the node at the head of the provided list
    :return: the head node of the sorted linked list
    """
    if length_iter(lnk)==0:
        return None
    new_node=LinkNode(find_min_value(lnk),None)
    lnk=remove(find_min_value(lnk),lnk)
    while length_iter(lnk)>0:
        new_node = LinkNode(find_min_value(lnk), new_node)
        lnk = remove(find_min_value(lnk), lnk)


    return reverse_rec(new_node)

def pretty_print( lnk ):
    """
    Print the contents of a linked list in standard Python format.
    [value, value, value] (Note the spaces.)
    :param lnk: the node at the head of the provided list
    :return: None
    """
    lst=[]
    while length_iter(lnk)>0:
        lst+=[lnk.value]
        lnk=remove(lnk.value,lnk)
    print(lst)


def find_min_value(lnk):
    """
    this function return the smallest value in sequence
    :param lnk: the node at the head of the provided list
    :return: the smallest value in the node
    """
    if length_iter(lnk)==1:
        return lnk.value
    else:
        z=lnk.value
        c=remove_at(0,lnk)
        k=c.value
        if z<k:
            Nlnk=remove(k,lnk)
        else:
            Nlnk=remove(z,lnk)

        return find_min_value(Nlnk)