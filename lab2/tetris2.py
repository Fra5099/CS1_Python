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


def B():
    """
    this function draws a shape like square
    :return:
    """
    tt.fillcolor('red')
    tt.begin_fill()
    block()
    tt.end_fill()

    tt.fd(20)
    tt.fillcolor('red')
    tt.begin_fill()
    block()
    tt.lt(90)
    tt.fd(20)
    tt.rt(90)
    block()
    tt.fd(-20)
    block()
    tt.rt(90)
    tt.fd(20)
    tt.lt(90)

    tt.end_fill()


def I():
    """
    this function draws a shape like I
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
    tt.rt(90)
    tt.fd(60)
    tt.lt(90)


def T():
    """
    this function draws specific shape like T
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
    tt.fd(-40)




def L():
    """
    this function draws specific shape like L

    :return:
    """
    tt.fillcolor('green')
    tt.begin_fill()
    block()
    tt.up()
    tt.fd(20)
    tt.down()
    block()
    tt.up()
    tt.fd(-20)
    tt.down()
    tt.lt(90)
    tt.fd(20)
    tt.rt(90)
    block()
    tt.lt(90)
    tt.fd(20)
    tt.rt(90)
    block()
    tt.end_fill()
    tt.rt(90)
    tt.fd(40)
    tt.lt(90)


def J():
    """
    this function draws specific shape like J

    :return:
    """
    tt.fillcolor('brown')
    tt.begin_fill()
    block()
    tt.end_fill()
    tt.fd(20)
    tt.fillcolor('brown')
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
    tt.up()
    tt.fd(-20)
    tt.rt(90)
    tt.fd(40)
    tt.lt(90)

def Z():
    """
    this function draws a shape like Z
    :return:
    """
    tt.fillcolor('gray')
    tt.begin_fill()
    block()
    tt.fd(20)
    block()
    tt.end_fill()
    tt.rt(90)
    tt.fd(20)
    tt.lt(90)
    tt.fillcolor('gray')
    tt.begin_fill()
    block()
    tt.fd(20)
    block()
    tt.end_fill()
    tt.up()
    tt.fd(-40)
    tt.lt(90)
    tt.fd(20)
    tt.rt(90)

def S():
    """
    this function draws a shape like S
    :return:
    """
    tt.fillcolor('pink')
    tt.begin_fill()
    block()
    tt.fd(20)
    block()
    tt.end_fill()
    tt.lt(90)
    tt.fd(20)
    tt.rt(90)
    tt.fillcolor('pink')
    tt.begin_fill()
    block()
    tt.fd(20)
    block()
    tt.end_fill()
    tt.up()
    tt.fd(-40)
    tt.rt(90)
    tt.fd(20)
    tt.lt(90)


def move(r,c):
    """
    this function goes to the place to draw the shape
    :param r: the number of row
    :param c: the number of column
    :return:
    """
    tt.up()
    tt.fd(20*c)
    tt.lt(90)
    tt.fd(20*r)
    tt.rt(90)
    tt.down()

def rotation(a):
    """
    this funtction to rotate the shape
    :param a: the angle of rotation
    :return:
    """
    tt.lt(a)

def datum_point(r,c,a):
    """

    :param r: the number of row
    :param c: the number of column
    :param a: the rotation angle
    :return:
    """

    tt.up()
    tt.rt(a)
    tt.lt(90)
    tt.fd(-20 * r)
    tt.rt(90)
    tt.fd(-20 * c)
    tt.down()


def shape(letter):
    """
    this function takes the input from the user to know which shape the user choose
    :param letter: str
    :return:
    """
    if letter=="B":
        return B()
    elif letter=="I":
        return I()
    elif letter=="L":
        return L()
    elif letter=="J":
        return J()
    elif letter=="Z":
        return Z()
    elif letter=="S":
        return S()
    elif letter=="T":
        return T()
    else:
        pass


def drawing_tetris_1():
    """
    this function draw tetris from the first lab
    :return:
    """
    B()
    move(0,2)
    T()
    datum_point(0,2,0)
    move(0,5)
    I()
    datum_point(0,5,0)
    move(0,6)
    B()
    datum_point(0,6,0)
    move(1,3)
    rotation(90)
    J()
    datum_point(1,3,90)
    move(3,4)
    rotation(90)
    I()
    datum_point(3,4,90)
    move(5,8)
    rotation(180)
    J()
    datum_point(5,8,180)
    move(1,9)
    rotation(90)
    T()
    datum_point(1,9,90)



def main():
    """
    this function draw the tetris
    :return:
    """
    board()
    drawing_tetris_1()
    letter=input("Enter a letter{BILJZST} to choose the shape to place:")
    a=int(input("Enter 0, 90, 180 or 270 for the rotation:"))
    print("Row and column is where to place lower left block of a shape.")
    r=int(input("Enter row number (0 to 19) for lower left space:"))
    c=int(input("Enter column number (0 to 9) for lower left space:"))
    move(r,c)
    rotation(a)
    shape(letter)
    datum_point(r,c,a)
    print("close the canvas window to quit")
    tt.done()

main()