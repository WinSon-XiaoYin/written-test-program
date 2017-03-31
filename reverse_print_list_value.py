# -*- coding:utf-8 -*-

class ListNode:
	def __init__(self, x):
		self.val = x
		self.next = None

class Link:
	def __init__(self, jd):
		self.head = jd
		self.head.next = None
		self.tail = self.head
		self.values = []

	def add(self, jd):
		self.tail.next = jd
		self.tail = self.tail.next

	def view(self):
		jd = self.head
		linkstr = ""
		while jd:
                    self.values.append(jd.val)
                    jd = jd.next
		    self.values = self.values[::-1]
	    	for i in self.values:
		    print i,


class Solution:
    # 返回从尾部到头部的列表值序列，例如[1,2,3]
    def printListFromTailToHead(self, listNode):
        # write code here
        return listNode.val
    
node1 = ListNode(10)
node2 = ListNode(4)
node3 = ListNode(2)

x = Link(node1)
x.add(node2)
x.add(node3)
x.view()

