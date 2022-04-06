"""
File: dna.py
Assignment: lab 08
Language: python3
Author: Faisal Alzahrany
Purpose: DNA Toolkit
CSCI 141
"""


from linked_code import*


def convert_to_nodes(strand):
    """
        this function convert the string (DNA) to nodes

    :param strand: string
    :return: linked sequence
    """
    if len(strand)==0:
        return None
    else:
        return LinkNode(strand[0],convert_to_nodes(strand[1:]))

def is_match(lnk1,lnk2):
    """
        this function check if the first DNA match the second DNA

    :param lnk1: the first linked sequence
    :param lnk2: the second linked sequence
    :return:
    """
    if lnk1 is None and lnk2 is None:
        return True
    elif lnk1 !=None and lnk2 == None or lnk2 != None and lnk1 == None:
        return False
    elif lnk1.value == lnk2.value:
        return is_match(lnk1.rest,lnk2.rest)
    else:
        return False


def insertion(lnk1, lnk2,index):
    """
    this function add sequence inside another sequence
    :param lnk1: the first linked sequence
    :param lnk2: the second linked sequence
    :param index: int
    :return: new linked sequence
    """
    if index > length_rec(lnk1):
        raise IndexError("invalid insertion index")
    elif index==0:
        return concatenate(lnk2,lnk1)
    else:
        return LinkNode(lnk1.value,(insertion(lnk1.rest,lnk2,index-1)))


def convert_to_string(dna):
    """
    this function convert the DNA sequence to a string
    :param dna: linked sequence
    :return: s:string
    """
    s=""
    (length_rec(dna))
    while 0<length_rec(dna):
        s+=dna.value
        dna=remove_at(0,dna)
    return s

def is_pairing(dna1,dna2):
    """
    this function check if the first DNA pair with the second DNA
    :param dna1: the first linked sequence
    :param dna2: the second linked sequence
    :return: boolean
    """
    if length_rec(dna1) != length_rec(dna2):
        return False
    elif dna1 is None and dna2 is None:
        return True
    else:
        dv1=dna1.value
        dv2=dna2.value
        if dna1.rest==None:
            if (dv1=="A" and dv2== "T") or (dv1=="T" and dv2=="A")\
                    or (dv1=="G" and dv2=="C") or (dv1=="C" and dv2=="G"):
                return True
            else:
                return False
        else:
            if (dv1 == "A" and dv2 == "T") or (dv1 == "T" and dv2 == "A" )\
                    or (dv1 == "G" and dv2 == "C") or (dv1 == "C" and dv2 == "G"):
                reDna1=remove(dv1,dna1)
                reDna2=remove(dv2,dna2)
                return is_pairing(reDna1,reDna2)
            else:
                return False


def is_palindrome(dna):
    """
        this function check if the DNA is palindrome
    :param dna: a linked sequence
    :return: boolean
    """
    if length_rec(dna)==0:
        return True
    else:
        re=reverse_rec(dna)
        First=dna.value
        Second=re.value
        while 0<length_rec(dna):

            First = dna.value
            Second = re.value
            if First != Second:
                return False
            else:
                dna=remove_at(0,dna)
                re=remove_at(0,re)
        return True

def substitution(dna,idx,base):
    """
        this function substitute a value in the sequence with another value
    :param dna: linked sequence
    :param idx: the index at which the substitution occurs
    :param segment_size: the new base to be substituted
    :return:
    """
    if idx > length_rec(dna):
        raise IndexError("invalid substitution index")
    elif idx==0:
        return LinkNode(base,dna.rest)
    else:
        return LinkNode(dna.value,(substitution(dna.rest,idx-1,base)))


def deletion(dna,idx,segment_size):
    """
        this function delete a number of elements from the sequence

    :param dna: linked sequence
    :param idx: the index at which deletion begins
    :param segment_size: the number of elments to be deleted
    :return: dna
    """
    if segment_size==0:
        return dna
    elif segment_size+idx >length_rec(dna):
        raise IndexError("invalid substitution index and segment size")
    else:
        new=remove_at(idx,dna)
        return deletion(new,idx,segment_size-1)




def duplication(dna,idx,segment_size):
    """
        this function duplicate specific elements inside the sequence

    :param dna: linked sequence
    :param idx: the index at which the segment to be duplicated begins
    :param segment_size: the number of elements to be deleted
    :return:    dna
    """
    if segment_size==0:
        return dna
    elif idx+segment_size>length_rec(dna):
        raise IndexError("invalid substitution index and segment size")
    else:
        if idx==0:
            d=deletion(dna,segment_size,length_rec(dna)-segment_size)

            return insertion(dna,d,idx)
        else:
            d1=deletion(dna,0,idx)
            d2=deletion(d1,segment_size,(length_rec(d1)- segment_size))
            dna=insertion(dna,d2,idx)
            return dna



