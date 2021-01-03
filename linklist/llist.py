# -*- coding: utf-8 -*-
from base_linklist import AbstractList,LNode


class LList(AbstractList):
    '''单链表 
    '''
    def __init__(self):
        self._head = None

    def is_empty(self):
        return self._head is None

    def get_length(self):
        p =  self._head
        length = 0
        while p!=0:
            length+=1
            p = p.next
        return length

    def prepend(self, elem):
        self._head = LNode(elem, self._head)

    def pop(self):
        if self._head is None:
            raise Exception('Underflow in pop')
        e = self._head.elem
        self._head = self._head.next
        return e

    def append(self, elem):
        if self._head is None:
            self._head = LNode(elem)
            return
        p = self._head
        while p.next is not None:
            p = p.next
        p.next = LNode(elem)

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
        return e

    def find(self, pred):
        p = self._head
        while p is not None:
            if pred(p.elem):
                return p.elem
            p = p.next

    def printall(self):
        p = self._head
        while p is not None:
            print(p.elem, end='')
            if p.next is not None:
                print(',', end='')
            p = p.next
        print('')

    def foreach(self, proc):
        p = self._head
        while p is not None:
            proc(p.elem)
            p = p.next

    def elements(self):
        p = self._head
        while p is not None:
            yield p.elem
            p = p.next

    def nodes(self):
        p = self._head
        while p is not None:
            yield p
            p = p.next

    def filter(self, pred):
        p = self._head
        while p is not None:
            if pred(p.elem):
                yield p.elem
            p = p.next

    def index(self, elem):pass#search
    def insert(self, elem, i):pass
    def get_item(self):pass
    def remove(self, i):pass#del
    

if __name__ == '__main__':
    mlist1 = LList()
    for i in range(10):
        mlist1.prepend(i)
    for i in range(11,20):
        mlist1.append(i)
    mlist1.printall()
    print('-------')
    mlist1.foreach(print)

    