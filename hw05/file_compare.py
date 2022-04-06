"""
File: file_compare.py
Assignment: homework
Language: python3
Author: Faisal Alzahrany
Purpose: comparing two different files in Python line by line character by character
CSCI 141
"""

def char_by_char(fname1,fname2):
    """
    This function compares two files character by character
    :param fname1:the name of first file
    :param fname2:the name of second file
    :return:
    """
    fn1=open(fname1)
    fn2=open(fname2)
    file_read1=open(fname1)
    file_read2=open(fname2)
    numCH1=0
    numCH2=0
    lineunm=0
    unCH=0
    unmatched=""
    lenL1=0
    lenL2=0



    for lines in file_read1: #this count the lines and the characters of first file
        lines=lines.strip()
        numCH1+=len(lines)
        lenL1+=1
    for lines2 in file_read2: #this count the lines and the characters of second file
        lines2=lines2.strip()
        numCH2+=len(lines2)
        lenL2+=1

    if  lenL1>=lenL2:
        extralines=(lenL1-lenL2)
        lineunm+=extralines
        stop=lenL2
    else:
        extralines = (lenL2 - lenL1)
        lineunm+=extralines
        stop=lenL1



    numlines=1
    while stop>=numlines: # here start comparing between the two files
        line=fn1.readline().strip()
        line2=fn2.readline().strip()
        accum = 0
        if len(line)>len(line2) or len(line2)>len(line): # when they have different length lines
            unmatched+=str(numlines)+", "
            lineunm+=1
        else: # when they have same length lines, comparing characters
            while len(line)>accum:
                if line[accum] !=line2[accum]:
                    unCH+=1
                    unmatched+=str(numlines)+":"+str(accum+1)+", "
                accum+=1
        numlines+=1
    accumExtra = 0
    while extralines > accumExtra: # if there extra lines than the other file

        unmatched += str(numlines) + ", "
        numlines+=1

        accumExtra+=1


    print("Character by character:")
    print("Unmatched characters: ",unmatched)
    print("There are",numCH1,"characters in",fname1)
    print("There are",numCH2,"characters in",fname2)
    print("There were",unCH,"unmatched characters in the files")
    print("There were",lineunm,"lines of different length")


def main():
    filename1=input("Enter the name of first file: ")
    filename2=input("Enter the name of second file: ")

    char_by_char(filename1,filename2)

main()