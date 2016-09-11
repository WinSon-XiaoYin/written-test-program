# -*- coding: utf-8 -*-

"""
二叉搜索树，满二叉树，由中序遍历重建二叉搜索树
"""

import copy

inputList = [1, 2, 3, 4, 5, 6, 7, 8, 9]

del1 = 1
del2 = 2
del3 = 4

class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None
        self.father = None

def buildTree(inputList, node=None):
    #mid = len(inputList)//2
    if len(inputList) != 0:
        mid = len(inputList)//2
        nodeNext = Node(inputList[mid])
        leftTree = inputList[:mid]
        rightTree = inputList[mid+1:]

        nodeNext.father = node
        nodeNext.left = buildTree(leftTree, nodeNext)
        nodeNext.right = buildTree(rightTree, nodeNext)
        return nodeNext
        
    else:
        return None 

def midFind(node):
    if node == None:
        return
    midFind(node.left)  
    print node.val
    midFind(node.right)

"""
mid = len(inputList)//2
node = Node(inputList[mid])
leftTree = inputList[:mid]
rightTree = inputList[mid+1:]

node.left = buildTree(leftTree, node)
node.right = buildTree(rightTree, node)
"""
node = buildTree(inputList)
midFind(node)
