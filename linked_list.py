# Perus haku algoja

from os import remove


numbers = [1,2,3,4,5,6,7,8,9,10]

def linear_search(list, target):
    for i in range(0, len(list)):
        if list[i] == target:
            return i
    return None


def verify(index):
    if index is not None:
        print("Target found at index: ", index)
    else:
        print("Target not found in list")

result = linear_search(numbers, 9)

verify(result)


def binary_search(list, target):
    first = 0
    last = len(list) -1

    while first <= last:
        midpoint = (first + last)//2
        if list[midpoint] == target:
            return midpoint
        elif list[midpoint] < target:
            first = midpoint +1
        else:
            last = midpoint -1

    return None

result = binary_search(numbers, 14)

verify(result)


def recursive_binary_search(list, target):
    if len(list) == 0:
        return False
    else:
        midpoint = (len(list))//2

        if list[midpoint] == target:
            return True

        else:
            if list[midpoint] < target:
                return recursive_binary_search(list[midpoint +1:], target)
            else:
                return recursive_binary_search(list[:midpoint], target)


result = recursive_binary_search(numbers, 3)

verify(result)


# Linked list settiä

class Node:
    data = None
    next_node = None

    def __init__(self,data):
        self.data = data

    def __repr__(self):
        return "<Node data: %s>" %self.data

class LinkedList:

    def __init__(self):
        self.head = None

    def is_empty(self):
        return self.head == None

    def size(self):
        current = self.head
        count = 0

        while current:
            count += 1
            current = current.next_node

        return count

    def add(self, data):
        new_node = Node(data)
        new_node.next_node = self.head
        self.head = new_node

    def search(self, key):
        current = self.head

        while current:
            if current.data == key:
                return current
            else:
                current = current.next_node

        return None

    def insert(self, data, index):
        if index == 0:
            self.add(data)

        if index > 0:
            new = Node(data)

            position = index
            current = self.head

            while position > 1:
                current = current.next_node
                position -= 1

            prev = current
            next_node = current.next_node

            prev.next_node = new
            new.next_node = next_node

    def remove(self,key):
        current = self.head
        previous = None
        found = False

        while current and not found:
            if current.data == key and current is self.head:
                found = True
                self.head = current.next_node
            elif current.data == key:
                found = True
                previous.next_node = current.next_node
            else:
                previous = current
                current = current.next_node

        return current

    def removeAt(self, index):
        current = self.head
        previous = None
        found = False

        if index > 0:
            position = index
            
            while position > 1:
                current = current.next_node
                position -= 1


l = LinkedList()
l.add(1)
l.add(2)
l.add(3)
l.add(4)
l.add(5)
l.add(6)
size = l.size()
n = l.search(5)


print(size)
print(n)
l.remove(4)
position = l.insert(10, 3)
size = l.size()
print(size)
