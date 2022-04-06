"""
File: anagram.py
Assignment: hw 09
Language: python3
Author: Faisal Alzahrany
Purpose: answering questions related to anagrams in the English language
CSCI 141
"""


def readfile(filename):
    """
    this function read the file and put the words inside dictionary
    :param filename: the name of the file we want to read
    :return: dictionary
    """
    file=open(filename)
    american={}
    for word in file:
        word=word.strip()
        lst=[]
        for ch in range(0,len(word)):
            lst+=[word[ch]]
        lst.sort()
        new_word=""
        for ch in range(0,len(lst)):
            new_word+=lst[ch]
        if new_word not in american:
            american[new_word]=[]
        american[new_word]+=[word]
    return american




def find_word(string,dic):
    """
    this function finds the list of anagrams inside american-english dictionary
    :param string: the word that we want to find its anagrams
    :param dic: american-english dictionary
    :return:
    """
    lst=[]
    word=""
    for ch in string:
        lst+=[ch]
    lst.sort()
    for ch in range(0,len(lst)):
        word+=lst[ch]
    if word not in dic:
        print("No words can be formed from:",string)
    else:
        print("Corresponding words:",dic[word])

def max_length(integer,dic):
    keys=dic.keys()
    max=0
    lst_name=""
    for name in keys:
        if len(name)==integer:
            if len(dic[name])>=max:
                max=len(dic[name])
                lst_name=name
    print("Max anagrams for length ",integer,":",max)
    print("Anagram list:",dic[lst_name])


def no_anagrams(integer,dic):
    """
    this function counts how many words with specific length does not have anagrams
    :param integer: the length of words
    :param dic: american-english dictionary
    :return:
    """
    keys=dic.keys()

    number=0
    for name in keys:
        if len(name)==integer:
            if len(dic[name])==1:
                number+=1

    print("Number of jumble usable words of length",integer,":",number)


def main():
    dic = readfile("american-english.txt")

    while True:
        word=input("Enter input string (hit enter key to go to task 3):")
        if word=="":
            break
        find_word(word,dic)
    print("")
    while True:
        length=input("Enter word length (hit enter key to go to task 4):")
        if length=="":
            break
        max_length(int(length),dic)
    print("")
    while True:
        number=input("Enter word length (hit enter key to quit):")
        if number=="":
            break
        no_anagrams(int(number),dic)

main()