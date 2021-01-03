#-*-coding:utf-8-*-
from abc import ABC,abstractmethod


class AbstractDict(ABC):
    @abstractmethod
    def is_empty(self):pass

    @abstractmethod
    def num(self):pass

    @abstractmethod
    def search(self, elem):pass#search

    @abstractmethod
    def insert(self, elem, i):pass

    @abstractmethod
    def delete(self, i):pass#del

    @abstractmethod
    def values(self):pass

    @abstractmethod
    def entries(self):pass

class Assoc:
    def __init__(self, key, value):
        self.key = key
        self.value = value

    def __lt__(self, other):
        return self.key < other.key

    def __le__(self, other):
        return self.key < other.key or self.key == other.key

    def __str__(self):
        return "Assoc({0}，{1})".format(self.key, self.value)