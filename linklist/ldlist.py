# -*- coding: utf-8 -*-
from base_linklist import AbstractList,LNode,LDNode
from ltlist import LTList

class LDList(LTList):
    '''双链表 
    '''
    def __init__(self):
        LTList.__init__(self)

    def prepend(self, elem):
        p = LDNode(elem, None, self._head)
        if self._head is None:
            self._rear = p
        else:
            p.next.prev = p
        self._head = p

    def append(self, elem):
        p= LDNode(elem, self._rear, None)
        if self._head is None:
            self._head = p
        else:
            p.prev.next = p
        self._rear = p

    def pop(self):
        if self._head is None:
            raise Exception('underflow pop in ldlist')
        e = self._head.elem
        self._head = self._head.next
        if self._head is not None:
            self._head.prev = None
        return e

    def pop_last(self):
        if self._head is None:
            raise Exception('underflow pop in ldlist')
        e = self._rear.elem
        self._rear = self._rear.prev
        if self._rear is None:
            self._head = None
        else:
            self._rear.next = None
        return e



if __name__ == '__main__':
    mlist1 = LDList()
    for i in range(10):
        mlist1.prepend(i)
    for i in range(11,20):
        mlist1.append(i)
    mlist1.printall()
    print('-------')
    mlist1.foreach(print)