#!/usr/bin/python3

"""This module contains classes that implements a singly linked list

classes:
    Node: Defines a node
    SinglyLinkedList: Defines operation sorted_insert to insert node
    to the list

Example:
    >>> sl = SinglyLinkedList()
    >>> sl.sorted_insert(3)
    >>> sl.sorted_insert(2)
    >>> sl.sorted_insert(1)
    >>> print(sl)
    1
    2
    3

"""


class Node:

    """Defines a node of a linked list

    Attribute:
        data: The data to store in the node (must be an integer)
        next_node: The instance of the next node (must be a Node object)
        or None

    Properties:
    data (setter and getter): store or retrieve the data stored in a node
    next_node (setter and getter): store or retrieve the instance
    of the next node

    """
    def __init__(self, data, next_node=None):
        self.data = data
        self.next_node = next_node

    @property
    def data(self):
        return self.__data

    @property
    def next_node(self):
        return self.__next_node

    @data.setter
    def data(self, value):
        if not isinstance(value, int):
            raise TypeError('data must be an integer')
        else:
            self.__data = value

    @next_node.setter
    def next_node(self, value):
        if not value or isinstance(value, Node):
            self.__next_node = value
        else:
            raise TypeError('next_node must be a Node object')


class SinglyLinkedList:

    """Implements a singly linked list

    Attribute:
        head: Instance of the first node in the list

    Methods:
        sorted_insert: Inserts a node into a linked list in an increasing order
        __str__: prints all the data in the linked list
        """

    def __init__(self):
        self.__head = None

    def sorted_insert(self, value):
        new_node = Node(value)

        temp = self.__head
        prev, beginning = None, True
        # get the position to insert
        while temp is not None and value > temp.data:
            prev, beginning = temp, False
            temp = temp.next_node

        if beginning:
            # inserting at the beginning
            new_node.next_node = temp
            self.__head = new_node
        else:
            # insert according to increasing order
            new_node.next_node = prev.next_node
            prev.next_node = new_node

    def __str__(self):
        temp = self.__head
        datas = []

        while temp:
            datas.append(temp.data)
            temp = temp.next_node

        return "\n".join(str(i) for i in datas)
