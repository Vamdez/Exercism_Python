class Node:
    def __init__(self, values = None, next = None):
        self.value = values
        self.next = next


class LinkedList:
    def __init__(self, values=[]):
        self.head = None
        self.values = values


    def insert_at_begining(self, values):
        node = Node(values, self.head)
        self.head = node

    def insert_at_end(self, values):
        if self.head is None:
            self.head = Node(values, None)
            return
        itr = self.head
        while itr.next:
            itr = itr.next
        itr.next = Node(values, None)
    
    def insert_multiples_values(self, list_values):
        for value in list_values:
            self.insert_at_end(value)

    def print(self):
        if self.head is None:
            print('Linked List is empty')
            return
        itr = self.head
        valuestr = ''
        while itr:
            valuestr += str(itr.value) + ' --> '
            itr = itr.next
        print(valuestr)

    def __len__(self):
        count = 0
        itr = self.head
        while itr:
            count += 1
            itr = itr.next
        print(count)

    def header(self):
        if self.head is None:
            print('Linked List is empty')
            return
        print(str(self.head.value))

    def pop(self, value_pop):
        if value_pop == self.head.value:
            self.head = self.head.next
            return
        itr = self.head
        count = 0
        while itr.value != value_pop:
            itr = itr.next
            count += 1
        itr = self.head
        while count > 1:
            count -= 1
            itr = itr.next
        itr.next = itr.next.next

    def reversed(self):
        pass


class EmptyListException(Exception):
    pass


ll = LinkedList()
ll.insert_at_begining(13)
ll.insert_multiples_values([10,20,30,40,50,60,70,80,90])
ll.pop(60)
ll.pop(80)
ll.__len__()
ll.print()