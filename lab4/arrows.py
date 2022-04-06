"""
Faisal Alzahrany
CSCI 141
"""

import turtle as tt

import random as rr


MAX_FIGURES=500
BOUNDING_BOX=200
MAX_DISTANCE=30
MAX_SIZE=30
MAX_ANGLE=30

def box():
    """
    this function draws the bounding box
    :return:
    """
    tt.up()
    tt.goto(-200,-200)
    tt.down()
    tt.fd(400)
    tt.lt(90)
    tt.fd(400)
    tt.lt(90)
    tt.fd(400)
    tt.lt(90)
    tt.fd(400)
    tt.lt(90)

def random_color():
    """
    this function return 3 random numbers to generate the RGB
    :return:
    """
    return rr.random(),rr.random(),rr.random()



def draw_figures_rec(depth,length=0):
    """
    this function draws the figures recursively
    :param depth: how many figures
    :param length: accumulator
    :return:
    """
    if depth<1:
        return length
    else:
        x = random_SIZE()
        box_borders(x)
        tt.down()
        tt.pencolor(random_color())
        tt.fillcolor(random_color())
        tt.begin_fill()
        tt.fd(x)
        tt.lt(120)
        tt.fd(x)
        tt.lt(120)
        tt.fd(x)
        tt.lt(120)
        tt.end_fill()
        tt.up()
        tt.fd(random_DISTANCE())
        tt.lt(random_ANGLE())
        length+=x

        return draw_figures_rec(depth-1,length)

def draw_figures_itr(depth):
    """
    this function draws the figures iteratively
    :param depth: how many figures
    :return:
    """
    length=0
    while depth>0:
        x = random_SIZE()
        box_borders(x)
        tt.down()
        tt.pencolor(random_color())
        tt.fillcolor(random_color())
        tt.begin_fill()
        tt.fd(x)
        tt.lt(120)
        tt.fd(x)
        tt.lt(120)
        tt.fd(x)
        tt.lt(120)
        tt.end_fill()
        tt.up()
        tt.fd(random_DISTANCE())
        tt.lt(random_ANGLE())
        length-=1
        depth-=1
        length+=x
    return length



def random_DISTANCE():
    """
    this function randomly generates the distance in range of 30
    :return:
    """
    return rr.randint(1,MAX_DISTANCE)

def random_SIZE():
    """
        this function randomly generates the size in range of 30

    :return:
    """
    return rr.randint(1,MAX_SIZE)

def random_ANGLE():
    """
        this function randomly generates the angle in range of 30

    :return:
    """
    return rr.randint(-MAX_ANGLE,MAX_ANGLE)




def box_borders(length):

    if tt.xcor() < -BOUNDING_BOX+MAX_DISTANCE or tt.ycor() < -BOUNDING_BOX+MAX_DISTANCE :
        tt.up()
        tt.rt(MAX_ANGLE*6)
        tt.fd(MAX_DISTANCE)
    elif tt.xcor() > BOUNDING_BOX-MAX_DISTANCE or tt.ycor()>BOUNDING_BOX-MAX_DISTANCE:
        tt.up()
        tt.lt(MAX_ANGLE * 6)
        tt.fd(MAX_DISTANCE)

    elif tt.xcor() > BOUNDING_BOX-MAX_DISTANCE or tt.ycor()<-BOUNDING_BOX+MAX_DISTANCE:
        tt.up()
        tt.lt(MAX_ANGLE * 6)
        tt.fd(MAX_DISTANCE)

    elif tt.xcor() < -BOUNDING_BOX+MAX_DISTANCE or tt.ycor()> BOUNDING_BOX-MAX_DISTANCE:
        tt.up()
        tt.rt(MAX_ANGLE * 6)
        tt.fd(MAX_DISTANCE)

    else:
        pass


def main():
    """
    main function promote the user to enter the number of figures and print the total area painted
    :return:
    """
    Arrows=int(input("Arrows (0-500) :"))
    if Arrows>MAX_FIGURES or Arrows<0:
        print("Arrows must be between 0 and 500 inclusive")
        pass
    else:
        box()
        print("The total area painted is",draw_figures_rec(Arrows,),"units.")
        input("Hit enter to continue...")
        tt.reset()
        box()
        print("The total area painted is",draw_figures_itr(Arrows),"units.")
        tt.done()
        print("Close the canvas window to quit")

main()