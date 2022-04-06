"""
141 Tree Lab - Derp the Interpreter

Derp is a simple interpreter that parses and evaluates prefix expressions 
containing basic arithmetic operators (*,//,-,+).  It performs arithmetic with
integer only operands that are either literals or variables (read from a 
symbol table).  It dumps the symbol table, produces the expression infix with 
parentheses to denote order of operation, and evaluates/produces the result of 
the expression.

Author: Scott C Johnson (scj@cs.rit.edu)

Author: Faisal Alzahrany
"""

from dataclasses import dataclass
from typing import Union

@dataclass
class LiteralNode:
    """Represents an operand node"""

    val: int


@dataclass
class VariableNode:
    """Represents a variable node"""

    name: str
    

@dataclass
class MathNode:
    """Represents a mathematical operation"""

    left: Union['MathNode', LiteralNode, VariableNode]
    op: str
    right: Union['MathNode', LiteralNode, VariableNode]


##############################################################################
# parse
############################################################################## 
    
def parse(tokens):
    """parse: list(String) -> Node
    From a prefix stream of tokens, construct and return the tree,
    as a collection of Nodes, that represent the expression.
    """
    if tokens==[]:
        raise IndexError
    token=tokens.pop(0)
    if token.isdigit():
        return LiteralNode(int(token))
    elif token.isidentifier():
        return VariableNode(token)
    else:
        left=parse(tokens)
        right=parse(tokens)
        return MathNode(left,token,right)

            
##############################################################################
# infix
##############################################################################
        
def infix(node):
    """infix: Node -> String | TypeError
    Perform an inorder traversal of the node and return a string that
    represents the infix expression."""
    if node is None:
        return " "
    elif isinstance(node,LiteralNode)==True:
        return str(node.val)
    elif isinstance(node,VariableNode)==True:
        return node.name
    else:

        left=infix(node.left)
        middle=str(node.op)
        right=infix(node.right)

    return "("+left+" "+middle+" "+right+")"

 
##############################################################################
# evaluate
##############################################################################    

def read_table(filename):
    """
    this function makes dictionary for the symbol table file
    :param filename: symbol table text
    :return: dic
    """
    file=open(filename)
    dic={}
    for line in file:
        line=line.split()
        if line[0] not in dic:
            dic[line[0]]=[]
        dic[line[0]]+=[int(line[1])]
    return dic




def evaluate(node, symTbl):
    """evaluate: Node * dict(key=String, value=int) -> int | TypeError
    Given the expression at the node, return the integer result of evaluating
    the node.
    Precondition: all variable names must exist in symTbl"""
    
    if node is None:
        return 0
    elif isinstance(node,LiteralNode)==True:
        return node.val
    elif isinstance(node,VariableNode)==True:
        return symTbl[node.name][0]
    else:

        left=evaluate(node.left,symTbl)
        middle=str(node.op)
        right=evaluate(node.right,symTbl)

        if middle=="+":
            return left+right
        elif middle=="-":
            return left-right
        elif middle=="*":
            return left*right
        elif middle=="//":
            return left//right
    
##############################################################################
# main
##############################################################################
                     
def main():
    """main: None -> None
    The main program prompts for the symbol table file, and a prefix 
    expression.  It produces the infix expression, and the integer result of
    evaluating the expression"""
    
    print("Hello Herp, welcome to Derp v1.0 :)")
    
    inFile = input("Herp, enter symbol table file: ")
    
    symTbl=read_table(inFile)
    
    print("Herp, enter prefix expressions, e.g.: + 10 20 (ENTER to quit)...")
    
    # input loop prompts for prefix expressions and produces infix version
    # along with its evaluation
    while True:
        prefixExp = input("derp> ")
        if prefixExp == "":
            break

        prefixExp=prefixExp.split()


        tree=parse(prefixExp)

        string=infix(tree)


        print("Derping the infix expression:",string)


        result=evaluate(tree,symTbl)

        print("Derping the evaluation:",result)
         
    print("Goodbye Herp :(")
    
if __name__ == "__main__":
    main()
