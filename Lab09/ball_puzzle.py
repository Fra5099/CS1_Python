"""
File: ball_puzzle.py
Assignment: lab 09
Language: python3
Author: Faisal Alzahrany
Purpose: solve the ball puzzle
CSCI 141
"""

from ball_puzzle_animate import *
from node import *
from dataclasses import *

def sort_cans(cans):
    """
    this function solve the ball puzzle by moving the balls by color to the can of specific color
    :param cans: list of 3 stacks
    :return: steps
    """
    steps=0
    count=cans[0].size
    while count>0:
        ball=top(cans[0])
        if ball=="G":
            push(cans[1],ball)
            pop(cans[0])
            animate_move(cans, 0, 1)
            steps+=1

        elif ball=="B":
            push(cans[2],ball)
            pop(cans[0])
            animate_move(cans,0,2)
            steps+=1


        else:
            if count==1:
                pass
            else:
                push(cans[1],ball)
                pop(cans[0])
                animate_move(cans,0,1)
                steps += 1

        count-=1
    count=cans[1].size
    while count>=1:
        ball=top(cans[1])
        if ball=="R":
            push(cans[0],ball)
            pop(cans[1])
            animate_move(cans,1,0)
            steps+=1
        else:
            if count==1:
                pass
            else:
                push(cans[2],ball)
                pop(cans[1])
                animate_move(cans,1,2)
                steps += 1

        count-=1

    count=cans[2].size
    while count>=1:
        ball=top(cans[2])
        if ball=="G":
            push(cans[1],ball)
            pop(cans[2])
            animate_move(cans,2,1)
            steps+=1


        else:
            break
        count-=1
    return steps

def main():
    RGB=input("Enter the colors of the balls(R,G,B):")

    animate_init(RGB)

    RED=make_empty_stack()
    GREEN=make_empty_stack()
    BLUE=make_empty_stack()
    cans=[RED,GREEN,BLUE]

    while len(RGB)>0:
        push(cans[0],RGB[0])
        RGB=RGB[1:]

    steps=sort_cans(cans)
    print("The number of moves needed to solve the problem:", steps)
    animate_finish()

main()