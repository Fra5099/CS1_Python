"""
Faisal Alzahrany
CSCI 141
"""

import turtle as tt

def block():
    """
    this function draws block
    :return:
    """
    tt.fd(20)
    tt.lt(90)
    tt.fd(20)
    tt.lt(90)
    tt.fd(20)
    tt.lt(90)
    tt.fd(20)
    tt.lt(90)


def board():
    """
    this function draws the board
    :return:
    """
    tt.up()
    tt.goto(-100,-100)
    tt.down()
    tt.fd(200)
    tt.lt(90)
    tt.fd(400)
    tt.lt(90)
    tt.fd(200)
    tt.lt(90)
    tt.fd(400)
    tt.lt(90)


def First_shape():
    """
    this function draws a shape like square
    :return:
    """
    tt.fillcolor('red')
    tt.begin_fill()
    block()
    tt.lt(90)
    block()
    tt.lt(90)
    block()
    tt.lt(90)
    block()
    tt.lt(90)
    tt.end_fill()


def Second_shape():
    """
    this function draws a shape like column
    :return:
    """
    tt.fillcolor('blue')
    tt.begin_fill()
    block()
    tt.lt(90)
    tt.fd(20)
    tt.rt(90)
    block()
    tt.lt(90)
    tt.fd(20)
    tt.rt(90)
    block()
    tt.lt(90)
    tt.fd(20)
    tt.rt(90)
    block()
    tt.end_fill()


def Third_shape():
    """
    this function draws specific shape like from Tetris game
    :return:
    """
    tt.fillcolor('yellow')
    tt.begin_fill()
    block()
    tt.fd(20)
    block()
    tt.end_fill()
    tt.up()
    tt.lt(90)
    tt.fd(20)
    tt.rt(90)
    tt.down()
    tt.fillcolor('yellow')
    tt.begin_fill()
    block()
    tt.up()
    tt.fd(20)
    tt.rt(90)
    tt.fd(20)
    tt.lt(90)
    tt.down()
    block()
    tt.end_fill()


def Fourth_shape():
    """
    this function draws specific shape like from Tetris game

    :return:
    """
    tt.fillcolor('green')
    tt.begin_fill()
    block()
    tt.end_fill()
    tt.fd(20)
    tt.fillcolor('green')
    tt.begin_fill()
    block()
    tt.lt(90)
    tt.fd(20)
    tt.rt(90)
    block()
    tt.lt(90)
    tt.fd(20)
    tt.rt(90)
    block()
    tt.end_fill()


def main():
    """
    this main function draws the Tetris game
    :return:
    """
    tt.speed(0)
    board()
    tt.up()
    tt.goto(-80,-80)
    tt.down()
    First_shape()
    tt.up()
    tt.fd(40)
    tt.lt(90)
    tt.down()
    Fourth_shape()
    tt.up()
    tt.rt(90)
    tt.goto(-60,-100)
    tt.down()
    Third_shape()
    tt.up()
    tt.fd(20)
    tt.down()
    Second_shape()
    tt.up()
    tt.goto(40, -80)
    tt.down()
    First_shape()
    tt.up()
    tt.fd(40)
    tt.lt(90)
    tt.down()
    Third_shape()
    tt.up()
    tt.rt(90)
    tt.goto(60,0)
    tt.lt(180)
    tt.down()
    Fourth_shape()
    tt.up()
    tt.rt(90)
    tt.goto(-20,-40)
    tt.down()
    Second_shape()
    tt.rt(90)
    tt.done()


main()
