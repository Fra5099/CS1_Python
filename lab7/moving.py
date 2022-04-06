
"""
File: store_location.py
Assignment: lab 07
Language: python3
Author: Faisal Alzahrany
Purpose: making 3 strategies for filling the boxes
CSCI 141
"""



from dataclasses import *

@dataclass()
class Item:
    name: str
    weight: int
@dataclass()
class Box:
    size:int
    items:list
    current:int

def creat(filename):
    """
    this function read the text file and convert the informations into list of items and boxes
    :param filename: the file text name
    :return:
    """
    box_weight=[]
    item_list=[]
    file=open(filename)

    for box in file.readline().split():
        x=Box(int(box),[],0)
        box_weight+=[x]

    while True:
        read=file.readline().split()
        if len(read)==0:
            break
        item_list+=[Item(read[0],int(read[1]))]


    return item_list,box_weight

def quick_sort_items( L ):#edition quick sort for the list of items
    """
    quickSort: List( A ) -> List( A )
        where A is 'totally ordered'
    """
    if L == []:
        return []
    else:
        pivot = L[0]
        ( less, same, more ) = partition_items( pivot, L )
        return quick_sort_items( less ) + same + quick_sort_items( more )

def partition_items( pivot, L ):
    """
    partition: A * List( A ) -> Tuple( List( A ), List( A ), List( A ) )
        where A is totally ordered
    """
    ( less, same, more ) = ( [], [], [] )
    for e in L:
        if e.weight > pivot.weight:
            less.append( e )
        elif e.weight < pivot.weight:
            more.append( e )
        else:
            same.append( e )
    return ( less, same, more )

def quick_sort_box( L ):#edition quick sort for the list of boxes
    """
    quickSort: List( A ) -> List( A )
        where A is 'totally ordered'
    """
    if L == []:
        return []
    else:
        pivot = L[0]
        ( less, same, more ) = partition_box( pivot, L )
        return quick_sort_box( less ) + same + quick_sort_box( more )

def partition_box( pivot, L ):
    """
    partition: A * List( A ) -> Tuple( List( A ), List( A ), List( A ) )
        where A is totally ordered
    """
    ( less, same, more ) = ( [], [], [] )
    for e in L:
        if e.size > pivot.size:
            less.append( e )
        elif e.size < pivot.size:
            more.append( e )
        else:
            same.append( e )
    return ( less, same, more )


def quick_sort_remaining( L ):#edition quick sort for the list of boxes that sort them by the greatest remaining
    """
    quickSort: List( A ) -> List( A )
        where A is 'totally ordered'
    """
    if L == []:
        return []
    else:
        pivot = L[0]
        ( less, same, more ) = partition_remaining( pivot, L )
        return quick_sort_remaining( less ) + same + quick_sort_remaining( more )

def partition_remaining( pivot, L ):
    """
    partition: A * List( A ) -> Tuple( List( A ), List( A ), List( A ) )
        where A is totally ordered
    """
    ( less, same, more ) = ( [], [], [] )
    for e in L:
        if e.current < pivot.current:
            less.append( e )
        elif e.current > pivot.current:
            more.append( e )
        else:
            same.append( e )
    return ( less, same, more )

def quick_sort_Lremaining( L ):#edition quick sort for the list of boxes that sort them by the least remaining
    """
    quickSort: List( A ) -> List( A )
        where A is 'totally ordered'
    """
    if L == []:
        return []
    else:
        pivot = L[0]
        ( less, same, more ) = partition_Lremaining( pivot, L )
        return quick_sort_Lremaining( less ) + same + quick_sort_Lremaining( more )

def partition_Lremaining( pivot, L ):
    """
    partition: A * List( A ) -> Tuple( List( A ), List( A ), List( A ) )
        where A is totally ordered
    """
    ( less, same, more ) = ( [], [], [] )
    for e in L:
        if e.current > pivot.current:
            less.append( e )
        elif e.current < pivot.current:
            more.append( e )
        else:
            same.append( e )
    return ( less, same, more )


def greedy_three(items,boxes):
    """
    this function sort the items inside the boxes from the largest item to the smallest
    and by filling the boxes one by one
    :param items: the list of items
    :param boxes: the list of boxes
    :return:
    """
    print("Results from Greedy Strategy 3")
    items=quick_sort_items(items)

    boxes=quick_sort_box(boxes)
    for box in boxes:
        extra_items = []
        for item in items:

            if box.size-box.current>=item.weight:
                box.items+=[item]
                box.current+=item.weight
            else:
                extra_items+=[item]
        items=extra_items

    if len(items)>0:
        print("Unable to pack all items!")
    num=1
    for box in boxes:
        print("Box",num,"of weight capacity",box.size,"contains:")
        for item in box.items:
            print(item.name,"of weight",item.weight)
    if len(items)>0:
        for item in items:
            print(item.name,"of weight",item.weight,"got left behind.")

def greedy_one(items,boxes):
    """
    this function sort the items inside the boxes from the largest item to the smallest
    and by the greatest remaining allowed weight
    :param items: the list of items
    :param boxes: the list of boxes
    :return:
    """
    print("Results from Greedy Strategy 1")

    items=quick_sort_items(items)
    boxes=quick_sort_box(boxes)
    extra_items=[]
    for item in items:
        boxes=quick_sort_remaining(boxes)
        count=0
        while len(boxes)>count:
            box=boxes[count]
            if box.size - box.current >= item.weight:
                box.items+=[item]
                box.current+=item.weight
                break
            if len(boxes)-1==count:
                extra_items+=[item]
            count+=1
    if len(extra_items)>0:
        print("Unable to pack all items!")
    num=1
    for box in boxes:
        print("Box",num,"of weight capacity",box.size,"contains:")
        for item in box.items:
            print(item.name,"of weight",item.weight)
    if len(extra_items)>0:
        for item in extra_items:
            print(item.name,"of weight",item.weight,"got left behind.")

def greedy_two(items,boxes):
    """
    this function sort the items inside the boxes from the largest item to the smallest
    and by the least remaining allowed weight
    :param items: the list of items
    :param boxes: the list of boxes
    :return:
    """
    print("Results from Greedy Strategy 2")

    items=quick_sort_items(items)
    boxes=quick_sort_box(boxes)
    extra_items=[]
    for item in items:
        boxes=quick_sort_Lremaining(boxes)
        count=0
        while len(boxes)>count:

            box=boxes[count]
            if box.size - box.current >= item.weight:
                box.items+=[item]
                box.current+=item.weight
                break
            if len(boxes)-1==count:
                extra_items+=[item]
            count+=1
    if len(extra_items)>0:
        print("Unable to pack all items!")
    num=1
    for box in boxes:
        print("Box",num,"of weight capacity",box.size,"contains:")
        for item in box.items:
            print(item.name,"of weight",item.weight)
    if len(extra_items)>0:
        for item in extra_items:
            print(item.name,"of weight",item.weight,"got left behind.")

def main():
    filename=input("Enter data filename: ")
    items,boxes=creat(filename)
    greedy_one(items,boxes)
    print("")
    items,boxes=creat(filename)
    greedy_two(items,boxes)
    print("")
    items,boxes=creat(filename)
    greedy_three(items,boxes)


main()