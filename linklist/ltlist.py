# -*- coding: utf-8 -*-
from base_linklist import LNode
from llist import LList

class LTList(LList):
    '''单链表  带尾部结点
    '''
    def __init__(self):
        self._head = None
        self._rear = None

    def prepend(self, elem):
        if self._head is None:
            self._head = LNode(elem, self._head)
            self._rear = self._head
        else:
            self._head = LNode(elem, self._head)

    def append(self, elem):
        if self._head is None:
            self._head = LNode(elem, self._head)
            self._rear = self._head
        else:
            self._rear.next = LNode(elem)
            self._rear = self._rear.next

    def pop_last(self):
        if self._head is None:
            raise Exception('Underflow in pop')
        p = self._head
        if p.next is None:
            e = p.elem
            self._head = None
            return e
        while p.next.next is not None:
            p = p.next
        e = p.next.elem
        p.next = None
        self._rear = p
        return e


if __name__ == '__main__':
    mlist1 = LTList()
    mlist1.prepend(99)
    for i in range(11,20):
        mlist1.append(i)
    print('-------')
    for x in mlist1.filter(lambda y: y%2==0):
        print(x)
