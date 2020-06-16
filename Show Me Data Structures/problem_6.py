class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

    def __repr__(self):
        return str(self.value)


class LinkedList:
    def __init__(self):
        self.head = None

    def __str__(self):
        cur_head = self.head
        out_string = ""
        while cur_head:
            out_string += str(cur_head.value) + " -> "
            cur_head = cur_head.next
        return out_string

    def append(self, value):

        if self.head is None:
            self.head = Node(value)
            return

        node = self.head
        while node.next:
            node = node.next

        node.next = Node(value)

    def size(self):
        size = 0
        node = self.head
        while node:
            size += 1
            node = node.next

        return size

    def to_list(self):
        node = self.head
        l = []
        while(node):
            l.append(node.value)
            node = node.next
        return l


def to_linked_list(list):
    ll = LinkedList()
    for i in list:
        ll.append(i)
    return ll


def union(llist_1, llist_2):
    # Your Solution Here
    l1 = llist_1.to_list()
    l2 = llist_2.to_list()
    final_list = list(set(l1+l2))
    return to_linked_list(final_list)


def intersection(llist_1, llist_2):
    # Your Solution Here
    l1 = set(llist_1.to_list())
    l2 = set(llist_2.to_list())
    final_list = []
    for i in l1:
        if i in l2:
            final_list.append(i)
    return to_linked_list(final_list)


# Test case 1
print("Case 1")
linked_list_1 = LinkedList()
linked_list_2 = LinkedList()

element_1 = [3, 2, 4, 35, 6, 65, 6, 4, 3, 21]
element_2 = [6, 32, 4, 9, 6, 1, 11, 21, 1]

for i in element_1:
    linked_list_1.append(i)

for i in element_2:
    linked_list_2.append(i)

print(union(linked_list_1, linked_list_2))
# 32 -> 65 -> 2 -> 35 -> 3 -> 4 -> 6 -> 1 -> 9 -> 11 -> 21 ->
print(intersection(linked_list_1, linked_list_2))
# 4 -> 6 -> 21 ->

# Test case 2
print("Case 2")
linked_list_3 = LinkedList()
linked_list_4 = LinkedList()

element_1 = [3, 2, 4, 35, 6, 65, 6, 4, 3, 23]
element_2 = [1, 7, 8, 9, 11, 21, 1]

for i in element_1:
    linked_list_3.append(i)

for i in element_2:
    linked_list_4.append(i)

print(union(linked_list_3, linked_list_4))
# 65 -> 2 -> 35 -> 3 -> 4 -> 6 -> 1 -> 7 -> 8 -> 9 -> 11 -> 21 -> 23 ->
print(intersection(linked_list_3, linked_list_4))
#

# Test case 3
print("Case 3")
linked_list_5 = LinkedList()
linked_list_6 = LinkedList()

element_1 = [20, 7, 4, 35, 6, 65, 6, 4, 3, 23]
element_2 = [1, 7, 8, 65, 11, 21, 1]

for i in element_1:
    linked_list_5.append(i)

for i in element_2:
    linked_list_6.append(i)

print(union(linked_list_5, linked_list_6))
# 65 -> 1 -> 35 -> 4 -> 3 -> 6 -> 7 -> 8 -> 11 -> 20 -> 21 -> 23 ->
print(intersection(linked_list_5, linked_list_6))
# 65 -> 7 ->

# Edges Cases
print("Edge Case 1")
linked_list_7 = LinkedList()
linked_list_8 = LinkedList()
element_1 = []
element_2 = [1, 7, 8, 65, 11, 21, 1]

for i in element_1:
    linked_list_7.append(i)

for i in element_2:
    linked_list_8.append(i)

print(union(linked_list_7, linked_list_8))
# 1 -> 65 -> 7 -> 8 -> 11 -> 21 ->
print(intersection(linked_list_7, linked_list_8))
#


print("Edge Case 2")
linked_list_9 = LinkedList()
linked_list_10 = LinkedList()
element_1 = []
element_2 = []

for i in element_1:
    linked_list_9.append(i)

for i in element_2:
    linked_list_10.append(i)

print(union(linked_list_9, linked_list_10))
#
print(intersection(linked_list_9, linked_list_10))
#
