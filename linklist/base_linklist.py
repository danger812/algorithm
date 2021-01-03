#-*-coding:utf-8-*-
from abc import ABC,abstractmethod


class AbstractList(ABC):
    @abstractmethod
    def is_empty(self):pass

    @abstractmethod
    def get_length(self):pass

    @abstractmethod
    def prepend(self,elem):pass

    @abstractmethod
    def append(self, elem):pass

    @abstractmethod
    def insert(self, elem, i):pass

    @abstractmethod
    def get_item(self):pass

    @abstractmethod
    def pop(self):pass

    @abstractmethod
    def pop_last(self):pass

    @abstractmethod
    def remove(self, i):pass#del

    @abstractmethod
    def index(self, elem):pass#search

    @abstractmethod
    def foreach(self, proc):pass

    def __getitem__(self, key):
        if self.is_empty():
            print('linklist is empty.')
            return
        elif key <0  or key > self.get_length():
            print('the given key is error')
            return
        else:
            return self.get_item(key)

    def __setitem__(self, key, value):
        if self.is_empty():
            print('linklist is empty.')
            return
        elif key <0  or key > self.get_length():
            print('the given key is error')
            return
        else:
            self.delete(key)
            return self.insert(key)


class LNode(object):
    def __init__(self, elem, next_=None):
        self.elem = elem
        self.next = next_


class LDNode(LNode):
    """docstring for LDNode"""
    def __init__(self, elem, prev=None, next_=None):
        super(LDNode, self).__init__(elem, next_)
        self.prev = prev
        


