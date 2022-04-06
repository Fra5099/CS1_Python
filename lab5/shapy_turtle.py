"""
File: shapy_turtle.py
Assignment: lab
Language: python3
Author: Faisal Alzahrany
Purpose: express turtle programs compactly as a string
CSCI 141
"""


import turtle as tt

def getNum(st):
    """this function gets the first number from the string"""
    if st=="":
        return (None,None)
    elif st[0].isdigit()==False:
        return (None,None)
    else:
        result=""
        y=""
        while st !="" and st[0].isdigit():

            result+=st[0]
            if len(st)==1:
                break
            elif st[1]==",":
                st=st[2:]
                y=result
                result=""
            else:
                st=st[1:]
        if result =="":
            return None
        else:
            if y=="" :
                delt=len(result)
                return (int(result),None,delt)
            else:
                delt=len(y)+len(result)+1
                return (int(y),int(result),delt)

def ShapyTurtle(st):
    """this function is interpreter for a shorthand language that allows you to express turtle programs as a string"""
    while st !="":
        cd=st[0]
        st=st[1:]

        if cd=="<":
            num=getNum(st)
            if num==(None,None):
                return None

            else:
                x,y,delt=num
                st = st[delt:]
                proLeft(x,y)

        elif cd==">":
            num = getNum(st)
            if num == (None, None):
                return None

            else:
                x, y, delt = num
                st = st[delt:]
                proRight(x,y)
        elif cd=="F":
            num = getNum(st)
            if num == (None, None):
                return None

            else:
                x, y, delt = num
                st = st[delt:]
                proFd(x,y)
        elif cd=="S":
            num = getNum(st)
            if num == (None, None):
                return None

            else:
                x, y, delt = num
                st = st[delt:]
                sqr(x,y)
        elif cd=="T":
            num = getNum(st)
            if num == (None, None):
                return None

            else:
                x, y, delt = num
                st = st[delt:]
                proTriangle(x,y)
        elif cd=="C":
            num = getNum(st)
            if num == (None, None):
                return None

            else:
                x, y, delt = num
                st = st[delt:]
                proCircle(x,y)
        elif cd=="B":
            num = getNum(st)
            if num == (None, None):
                return None

            else:
                x, y, delt = num
                st = st[delt:]
                proBack(x,y)
        elif cd=="U":
            tt.up()
        elif cd=="D":
            tt.down()
        elif cd=="R":
            num = getNum(st)
            if num == (None, None):
                return None

            else:
                x, y, delt = num
                st = st[delt:]
                proRectangle(x,y)
        elif cd=="P":
            num = getNum(st)
            if num == (None, None):
                return None

            else:
                x, y, delt = num
                st = st[delt:]
                proPolygon(x,y)
        elif cd=="G":
            num = getNum(st)
            if num == (None, None):
                return None

            else:
                x, y, delt = num
                st = st[delt:]
                proGoto(x,y)
        elif cd=="Z":
            num = getNum(st)
            if num == (None, None):
                return None

            else:
                x, y, delt = num
                st = st[delt:]
                proColor(x,y)
        else:
            print("Error, a valid ShapyTurtle command")
            break



def proLeft(x,y):
    """this function turn left for some degree"""
    tt.left(x)

def proRight(x,y):
    """this function turn right for some degree """
    tt.right(x)

def proFd(x,y):
    """this function move forward"""
    tt.fd(x)

def sqr(x,y):
    """this function draws square"""

    tt.fd(x)
    tt.lt(90)
    tt.fd(x)
    tt.lt(90)
    tt.fd(x)
    tt.lt(90)
    tt.fd(x)
    tt.lt(90)

def proTriangle(x,y):
    """this function makes triangle"""

    tt.fd(x)
    tt.lt(120)
    tt.fd(x)
    tt.lt(120)
    tt.fd(x)
    tt.lt(120)

def proCircle(x,y):
    """this function makes circle"""

    tt.circle(x)

def proBack(x,y):
    """this function moves backward"""

    tt.bk(x)

def proRectangle(l,w):
    """this function draws Rectangle"""
    tt.fd(w)
    tt.lt(90)
    tt.fd(l)
    tt.lt(90)
    tt.fd(w)
    tt.lt(90)
    tt.fd(l)
    tt.lt(90)

def proPolygon(s,l):
    """this function draws any polygon"""

    if s is None or l is None:
        return None
    else:
        angs=360/s
        while s >0:
            tt.fd(l)
            tt.lt(angs)
            s=s-1

def proGoto(x,y):
    """this function goes to specific point"""


    tt.goto(x,y)

def proColor(x,y):
    """this function change the color of the pen"""
    if x==0:
        tt.pencolor("red")
    elif x==1:
        tt.pencolor("blue")
    elif x==2:
        tt.pencolor("green")
    elif x==3:
        tt.pencolor("yellow")
    elif x==4:
        tt.pencolor("brown")
    else:
        tt.pencolor("black")

def main():
    words=str(input("Enter the commands of ShapyTurtle:"))
    ShapyTurtle(words)
    tt.done()


main()
