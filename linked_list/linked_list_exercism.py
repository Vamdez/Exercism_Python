from audioop import reverse
from cmath import tau


class Node:
    def __init__(self, values = None, next = None):
        self.data = values
        self.prox = next

    def value(self):
        return self.data

    def next(self):
        return self.prox


class LinkedList:
    def __init__(self, values=[]):
        self.header = None
        self.insert_multiples_values(values)

    def __len__(self):
        count = 0
        itr = self.header
        while itr:
            count += 1
            itr = itr.prox
        return count
        
    def head(self):
        if self.header is None:
            raise EmptyListException("The list is empty.")
        return(self.header)
        
    def insert_multiples_values(self, list_values):
        for value in list_values:
            self.push(value)
            
    def push(self, values):
        node = Node(values, self.header)
        self.header = node

    def pop(self):
        if self.header is None:
            raise EmptyListException("The list is empty.")
        pop_value = self.header
        self.header = self.header.prox
        return pop_value.data

    def reversed(self):
        tail_for_head = []
        itr = self.header
        while itr:
            tail_for_head.append(itr.data)
            itr = itr.prox
        tail_for_head.reverse()
        return tail_for_head

    def __iter__(self):
        itr = self.header
        while itr:
            yield itr.data
            itr = itr.prox


class EmptyListException(Exception):
    def __init__(self, message):
        self.message = message

ll = LinkedList([1,3,4,6,8,12,34])
print(ll.reversed())
