#-*-coding:utf-8-*-
from base_stackqueue import AbstractStack,LNode


class SStack(AbstractStack):
    '''栈 --顺序存储
    '''
    def __init__(self):
        self._elems = []

    def is_empty(self):
        return self._elems == []

    def top(self):
        if self._elems == []:
            raise Exception('under flow in stack top ')
        return self._elems[-1]

    def push(self, elem):
        self._elems.append(elem)

    def pop(self): #默认移除最后一个元素
        if self._elems == []:
            raise Exception('under flow in stack top ')
        return self._elems.pop()


class LStack(AbstractStack):
    ''' 栈--- 链式存储
    '''
    def __init__(self):
        self._top = None

    def is_empty(self):
        return self._top is None

    def top(self):
        if self._top is None:
            raise Exception('under flow in stack top ')
        return self._top.elem

    def push(self, elem):
        self._top = LNode(elem, self._top)

    def pop(self):
        if self._top is None:
            raise Exception('under flow in stack top ')
        p = self._top
        self._top = p.next
        return p.elem


if __name__ == '__main__':
    st1 = SStack()
    st1.push(3)
    st1.push(5)
    while not st1.is_empty():
        print(st1.pop())
    lt1 = LStack()
    lt1.push(4)
    lt1.push(5)
    while not lt1.is_empty():
        print(lt1.pop())