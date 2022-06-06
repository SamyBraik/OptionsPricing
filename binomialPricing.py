import math as m

FP = list()

class Node:
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None

#Construction of the binary search tree
def construction(node,u,v):
        if node.left == None and node.right == None:
            node.left = Node(node.key*v)
            node.right = Node(node.key*u)
        else:
            construction(node.left,u,v)
            construction(node.right,u,v)

#Extraction of the values contained in the leafs into the list FP
def extraction(node):
    if node.left == None and node.right == None:
        if round(node.key,4) not in FP:
            FP.append(round(node.key,4))
    else:
        extraction(node.right)
        extraction(node.left)
    return FP


#Calculate the option value using delta hedging
def optionValue(E,r,T,t,S,u,v):
    root = Node(S)
    for i in range(0,T):
        construction(root,u,v)
    extraction(root)
    delta = (max(FP[0]-E,0)-max(FP[1]-E,0))/(FP[0]-FP[1])
    return (max(FP[0]-E,0) -delta*(FP[0]))*m.exp(-r*(T-t)) + delta*S


