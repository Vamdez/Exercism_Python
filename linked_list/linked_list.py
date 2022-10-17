class Node:
    def __init__(self, value, next_node = None):
        self.value = value
        self.next_node = next_node

    def value(self):
        pass

    def next(self):
        pass


class LinkedList:
    def __init__(self, values=[]):
        self.head = None
        self.tail = None
        if values:
            self.add_multiples_nodes(values)

    def __len__(self):
        pass

    def head(self):
        pass

    def push(self, value):
        pass

    def pop(self):
        pass

    def reversed(self):
        pass


class EmptyListException(Exception):
    pass