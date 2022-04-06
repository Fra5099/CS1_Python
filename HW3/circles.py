"""
File: circles.py
Assignment: homework
Language: python3
Author: Faisal Alzahrany
CSCI 141
"""

import turtle as tt


def circles(length,depth):
    """
    this function draws circles depends on how many depths the user enter
    :param length:the radius of the circle
    :param depth:the number of circles
    :return:
    """
    if depth==0:
        pass
    elif depth==1:
        tt.down()
        tt.circle(length)
    else:
        tt.down()
        tt.circle(length)
        tt.up()
        tt.fd(length)
        tt.lt(90)
        tt.fd(length)
        tt.rt(90)
        circles(length / 2, depth - 1)
        tt.up()
        tt.fd(-2*length)
        circles(length / 2, depth - 1)
        tt.up()
        tt.fd(length)
        tt.rt(90)
        tt.fd(length)
        tt.lt(90)


def main():
    circles(100,4)
    tt.done()

main()

