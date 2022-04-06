"""
Faisal Alzahrany
CSCI 141
"""

import turtle as tt

def draw_one_bowtie(size):
    """
    this function draws one bowtie
    :param size: the length of one side of the triangle
    :return:
    """
    tt.down()
    tt.up()
    tt.pencolor("blue")
    tt.lt(90)
    tt.fd(size/4)
    tt.rt(90)
    tt.down()
    tt.lt(30)
    tt.fd(size)
    tt.rt(120)
    tt.fd(size)
    tt.rt(120)
    tt.fd(2*size)
    tt.lt(120)
    tt.fd(size)
    tt.lt(120)
    tt.fd(size)
    tt.up()
    tt.rt(120)
    tt.fd(size/4)
    tt.lt(90)
    tt.down()
    tt.fillcolor("red")
    tt.begin_fill()
    tt.circle(size / 4)
    tt.end_fill()
    tt.up()
    tt.lt(90)
    tt.fd(size/4)
    tt.rt(90)

def draw_bowties(size,depth):
    """
    this function draws bowties
    :param size: the length of one side of the triangle
    :param depth: how many bowties
    :return:
    """
    if depth==0:
        pass
    if depth==1:
        draw_one_bowtie(size)
    else:
        draw_one_bowtie(size)
        tt.up()
        tt.lt(30)
        tt.fd(size * 2)
        draw_bowties(size / 3, depth - 1)
        tt.up()
        tt.fd(-2 * size)
        tt.lt(120)
        tt.fd(size*2)
        draw_bowties(size / 3, depth - 1)
        tt.up()
        tt.fd(-2*size)
        tt.lt(60)
        tt.fd(2*size)
        draw_bowties(size/3,depth-1)
        tt.up()
        tt.fd(-2*size)
        tt.lt(120)
        tt.fd(2*size)
        draw_bowties(size/3,depth-1)
        tt.up()
        tt.fd(-2*size)
        tt.lt(30)

def main():
    """
    main function
    :return:
    """

    draw_bowties(int(input("The size of bowtie:")),int(input("Depths:")))
    tt.done()


main()