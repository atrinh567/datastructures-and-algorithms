class Array:
    def __init__(self, arr=[]):
        self.arr = []

    def append(self, num):
        self.arr.append(num)

    def delete(self, target):
        for i in self.arr:
            if target == i:
                self.arr.remove(i)

    def deleteAtIndex(self, idx):
        return self.arr.pop(idx)

    def pop(self, idx=0):
        if len(self.arr) > 0:
            return self.arr.pop(idx)
        return

    def push(self, num):
        self.append(num)

    def find(self, target):
        for i in self.arr:
            if target == i:
                return True
        return False

    def index(self, target):
        for i in range(0, len(self.arr)):
            if target == self.arr[i]:
                return i
        return -1

    def __len__(self):
        return len(self.arr)

    def __str__(self):
        s = ""
        if len(self.arr) != 0:
            for i in self.arr:
                s += str(i) + " "
        return s.rstrip()
