#-*-coding:utf-8-*-
from abc import ABC,abstractmethod

class AbstractStack(ABC):
    @abstractmethod
    def is_empty(self):pass

    @abstractmethod
    def push(self, elem):pass

    @abstractmethod
    def pop(self):pass

    @abstractmethod
    def top(self):pass


class AbstractQueue(ABC):
    @abstractmethod
    def is_empty(self):pass

    @abstractmethod
    def enqueue(self,elem):pass

    @abstractmethod
    def dequeue(self):pass

    @abstractmethod
    def peek(self):pass


class LNode(object):
    def __init__(self, elem, next_=None):
        self.elem = elem
        self.next = next_