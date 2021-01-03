#-*-coding:utf-8-*-
from base_dict import AbstractDict,Assoc


class ListDict(AbstractDict):
    '''顺序表实现
    '''
    def __init__(self):
        self._elems = []

    def is_empty(self):
        return not self._elems

    def num(self):
            return len(self._elems)

    def search(self, key):
        for item in self._elems:
            if item.key == key:
                break
        return item.value

    def insert(self, key, value):
        new_item = Assoc(key, value)
        for i in range(len(self._elems)):
            item = self._elems[i]
            if item.key == key:
                self._elems[i] = new_item
                break
        else:
            self._elems.append(new_item)

    def delete(self, key):
        for i in range(len(self._elems)):
            item = self._elems[i]
            if item.key != key:
                continue
            self._elems.pop(i)
            break

    def values(self):
        for item in self._elems:
            yield item.value

    def entries(self):
        for item in self._elems:
            yield item.key,item.value


class OrdListDict(ListDict):
    '''有序顺序表实现
    '''
    def search(self, key):
        ind, succ = self._get_bin_index(key)
        if succ:
            return self._elems[ind].value

    def insert(self, key, value):
        item = Assoc(key, value)
        if len(self._elems) == 0:
            self._elems.append(item)
            return
        ind, succ = self._get_bin_index(key)
        if succ:
            self._elems[ind] = item
        else:
            self._elems.append(None)
            for i in range(len(self._elems) - 2, ind-1, -1):
                if i == ind:
                    if item.key > self._elems[ind].key:
                        self._elems[i + 1] = item
                    else:
                        self._elems[i + 1] = self._elems[i]
                        self._elems[i] = item
                else:
                    tmp = self._elems[i]
                    self._elems[i + 1] = tmp

    def delete(self, key):
        ind, succ = self._get_bin_index(key)
        if succ:
            self._elems.pop(ind)

    def _get_bin_index(self, key):
        lst = self._elems
        low, high = 0, len(lst) - 1
        mid, succ = 0, False
        while low <= high:
            mid = low + (high - low) // 2
            if key == lst[mid].key:
                succ = True
                break
            if key < lst[mid].key:
                high = mid - 1
            else:
                low = mid + 1
        return mid, succ


if __name__ == '__main__':
    dl = ListDict()
    #dl = OrdListDict()
    dl.insert(2,3)
    dl.insert(1,2)
    dl.insert(2,4)
    dl.insert(5,4)
    dl.insert(3,4)
    dl.delete(1)
    for k, v in dl.entries():
        print('item', k, v)
    print('search: ' + str(dl.search(2)))