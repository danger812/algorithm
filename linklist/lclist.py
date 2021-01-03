# -*- coding: utf-8 -*-
from base_linklist import AbstractList,LNode

class LinkCList(AbstractList):
    '''循环 单链表
    '''
    def __init__(self):
        self._rear = None

    def is_empty(self):
        return self._rear == 0

    def prepend(self,item):
        p = LNode(item)
        if self._rear is None:
            p.next = p
            self._rear = p
        else:
            p.next = self._rear.next
            self._rear.next = p

    def append(self,item):
        self.prepend(item)
        self._rear = self._rear.next

    def pop(self):
        if self._rear is None:
            raise Exception('in pop of cllist')
        p = self._rear.next
        if self._rear is p:
            self._rear = None
        else:
            self._rear.next = p.next
        return p.data

    def get_item(self, index):pass
    def insert(self, index, item): pass
    def remove(self, i):pass#del
    def index(self, elem):pass#search
    def get_length(self):pass
    def pop_last(self):pass

    def printall(self):
        if self.is_empty():
            return
        p = self._rear.next
        while p is not None:
            print(p.elem, end='')
            if p is self._rear:
                break
            p = p.next
        print('')

    def foreach(self, proc):
        p = self._rear.next
        while p is not self._rear:
            proc(p.elem)
            p = p.next

if __name__ == '__main__':
    mlist1 = LinkCList()
    for i in range(10):
        mlist1.prepend(i)
    for i in range(11,20):
        mlist1.append(i)
    mlist1.printall()
    print('-------')
    mlist1.foreach(print)