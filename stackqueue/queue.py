#-*-coding:utf-8-*-
from base_stackqueue import AbstractQueue, LNode


class SQueue(AbstractQueue):
    '''队列--- 顺序存储
    '''
    def __init__(self, init_len=8):
        self._len = init_len
        self._elems = [0] * init_len
        self._head = 0 #队首，如果有元素出队 则向后移动一位
        self._num = 0 #元素个数

    def is_empty(self):
        return self._num == 0

    def enqueue(self,elem):
        if self._num == self._len:
            self.__extend()
        self._elems[(self._head+self._num)%self._len] = elem #循环向数组中入队和出队
        self._num += 1

    def dequeue(self):
        if self._num == 0:
            raise Exception('under flow in squeue peek')
        e = self._elems[self._head]
        self._head = (self._head + 1) % self._len
        self._num -= 1
        return e

    def peek(self):
        if self._num == 0:
            raise Exception('under flow in squeue peek')
        return self._elems[self._head]

    def __extend(self):
        old_len = self._len
        self._len *= 2
        new_elems = [0] * self._len
        for i in range(old_len):
            new_elems[i] = self._elems[(self._head+i)%self._len]
        self._elems, self._head = new_elems, 0
    

class LQueue(AbstractQueue):
    '''队列 --- 链式存储
    '''
    def __init__(self):
        self._head = None # 队首，如果有元素出队则向后移动一位
        self._rear = None # 队位，如果有元素入队则向后移动一位

    def is_empty(self):
        return self._head is None

    def enqueue(self, elem):
        if self._head is None:
            self._head = LNode(elem, self._head)
            self._rear = self._head
        else:
            self._rear.next = LNode(elem)
            self._rear = self._rear.next

    def dequeue(self):
        if self._head is None:
            raise Exception('Underflow in pop')
        e = self._head.elem
        self._head = self._head.next
        return e

    def peek(self):
        if self._head is None:
            raise Exception('Underflow in pop')
        e = self._head.elem
        return e


if __name__ == '__main__':
    sq1 = SQueue()
    sq1.enqueue(4)
    sq1.enqueue(6)
    while not sq1.is_empty():
        print(sq1.dequeue())