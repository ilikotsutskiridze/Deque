import sys
import re


class Deque:
    def __init__(self):
        self.deque = None
        self.size = 0
        self.capacity = 0
        self.head = 0
        self.tail = 0

    def pop_back(self):
        if self.deque is None:
            return 'error'
        elif self.size == 0:
            return 'underflow'
        else:
            if self.tail == 0:
                self.tail = self.capacity
            self.tail -= 1
            self.size -= 1
            element = self.deque[self.tail]
            return element

    def pop_front(self):
        if self.deque is None:
            return 'error'
        if self.size == 0:
            return 'underflow'
        else:
            element = self.deque[self.head]
            self.head += 1
            self.size -= 1
            if self.head == self.capacity:
                self.head = 0
            return element

    def set_size(self, n):
        if self.deque is not None:
            print('error')
        else:
            self.deque = [None] * n
            self.capacity = n

    def print(self):
        if self.deque is None:
            print('error')
        elif self.size == 0:
            print('empty')
            return
        else:
            element_pos = self.head
            for i in range(self.size):
                print(self.deque[element_pos], end=' ') if i != (self.size - 1) else print(self.deque[element_pos])
                element_pos += 1
                if element_pos == self.capacity:
                    element_pos = 0

    def push_front(self, element):
        if self.deque is None:
            print('error')
        elif self.size == self.capacity:
            print('overflow')
        else:
            if self.head == 0:
                self.head = self.capacity
            self.head -= 1
            self.size += 1
            self.deque[self.head] = element

    def push_back(self, element):
        if self.deque is None:
            print('error')
        elif self.size == self.capacity:
            print('overflow')
        else:
            self.deque[self.tail] = element
            self.size += 1
            self.tail += 1
            if self.tail == self.capacity:
                self.tail = 0


if __name__ == '__main__':
     
    Bl = Deque()

    array = []
    for line in sys.stdin.readlines():
        if len(re.findall(r'.+', line)) != 0:
            array.append(str(re.findall(r'.+', line)[0]))

    for i in range(len(array)):
         if re.match(r'^(pushb|pushf)\s\S+$', array[i]):
            arr = str(array[i]).split(" ")
            if arr[0] == 'pushb':
                Bl.push_back(arr[1])
            elif arr[0] == 'pushf':
                Bl.push_front(arr[1])
         elif re.match(r'^(popb|popf)$', array[i]):
            if array[i] == 'popb':
                 print(Bl.pop_back())
            elif array[i] == 'popf':
                 print(Bl.pop_front())
         elif re.match(r'^set_size\s\d+$', array[i]):
            arr = array[i].split()
            Bl.set_size(int(arr[1]))
         elif re.match(r'^print$', array[i]):
            Bl.print()
         elif array[i] != "":
            print('error')
    del array
