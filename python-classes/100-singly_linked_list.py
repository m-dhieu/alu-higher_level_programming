#!/usr/bin/python3


"""This module enlightens on Singlylinkedlist."""


class Node:
    """Represent a Node."""
    
    def __init__(self, data, next_node=None):
        """Initialize a Node object."""
        self.data = data
        self.next_node = next_node

    @property
    def data(self):
        """Retrieve the data of the node."""
        return self.__data

    @data.setter
    def data(self, value):
        """Set the data of the node."""
        if not isinstance(value, int):
            raise TypeError("data must be an integer")
        self.__data = value

    @property
    def next_node(self):
        """Retrieve the next node in the list."""
        return self.__next_node

    @next_node.setter
    def next_node(self, value):
        """Set the next node in the list."""
        if not (value is None or isinstance(value, Node)):
            raise TypeError("next_node must be a Node object")
        self.__next_node = value


class SinglyLinkedList:
    def __init__(self):
        """Initialize a SinglyLinkedList object."""
        self.__head = None

    def __str__(self):
        """Print the entire list in stdout.
        One node number by line."""
        current = self.__head
        while current:
            print(current.data)
            current = current.next_node

    def sorted_insert(self, value):
        """Insert a new Node into the correct sorted position in the list."""
        new_node = Node(value)

        if not self.__head or self.__head.data >= value:
            new_node.next_node = self.__head
            self.__head = new_node
            return

        current = self.__head
        while current.next_node and current.next_node.data < value:
            current = current.next_node

        new_node.next_node = current.next_node
        current.next_node = new_node
