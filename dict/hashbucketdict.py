#-*-coding:utf-8-*-
import sys
sys.path.append('../linklist')
from llist import LList
from base_dict import AbstractDict
# -----外消解-桶散列 散列方式 实现 dict[hashbucketdict]
# 冲突解决:分离链--冲突位置排成一个链; linear probing发生冲突去下一个位置

# hash每个位置被称为slot槽。可以使用list实现hash,每个slot对应一个key,存放元素
class HashBucketDict(AbstractDict):
    '''冲突外消解-桶散列法
    '''
    def __init__(self):
        self.size = 11
        self.slots = [None] * self.size
        self.data = [LList()] * self.size

    def put(self, key, data):
        hashvalue = self.hashfunction(key, self.size)

        if self.slots[hashvalue] == None:
            self.slots[hashvalue] = key
            self.data[hashvalue].append((key,data))
        else:
            for nd in self.data[hashvalue].nodes():
                if nd.elem[0] == key:
                    nd.elem = (key,data)         # 替换相同索引对应的项目
                    break
            else:
                self.data[hashvalue].append((key,data))

    #def hashfunction(self, key, size): # 散列方法 - 求余【基于整数】
    #    return key%size

    def hashfunction(self, key, size): # 散列方法 - 求余 【基于非整数】
        return hash(str(key))%size

    def rehash(self, oldhash, size): # 内消解-开地址法-线性探查法
        return (oldhash+1)%size

    #def rehash(self, oldhash, size): # 内消解-开地址法-双散列探查法
    #    return (oldhash+6)%size

    def get(self, key):
        startslot = self.hashfunction(key, len(self.slots))

        data = None
        stop = False
        position = startslot
        while self.slots[position] != None and not stop:
            for nd in self.data[position].nodes():
                if nd.elem[0] == key:
                    data = nd.elem[1]
                    stop = True
                    break
            else:
                stop = True
        return data

    def __getitem__(self, key):
        return self.get(key)

    def __setitem__(self, key, data):
        self.put(key, data)
    def is_empty(self):pass
    def num(self):pass
    def delete(self, key):pass#del
    def values(self):pass
    def entries(self):pass
    def insert(self):pass
    def search(self):pass

if __name__ == '__main__':
    H = HashBucketDict()
    #H['abc'] = 'cat'
    H[54] = 'cat'
    H[26] = "dog"
    H[93] = "lion"
    H[17] = "tiger"
    H[77] = "bird"
    H[31] = "cow"
    H[44] = "goat"
    H[55] = "pig"
    H[20] = "chicken"
    print(H[20])
    print(H.slots)
    print(H.data)
    print(H[99])
    H[21] = "elephant"
    H[22] = "sheep"
    H[23] = "fish"
    print(H.data)
    H[20] = 'monkey'
    print(H[20])