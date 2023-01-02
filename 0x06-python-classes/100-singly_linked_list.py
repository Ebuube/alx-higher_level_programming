#!/usr/bin/python3
"""This module implements a singly linked list ADT

Attributes:
    Node (class): represents a node object
    SinglyLinkedList (class): represents a list object
"""


class SinglyLinkedList:
    """Represents a singly linked list object

    Attributes:
        Node (class): represents a node object
        __head (Node): head of the list
    """



# work to do, properly insert this class Node into class SinglyLinkedList


class Node:
    """Represents a node object

    Attributes:
        __data (int): data stored in the node
        __next_node (Node): points to the next node object in the list
    """

    def __init__(self, data, next_node=None):
        """Initialize a new node object

        The argument data must be an integer otherwise it raises a TypeError
        exception with message `data must be an integer`
        The argument `next_node` must be None or a Node object, otherwise
        it raises a TypeError exception with the message `next_node must be
        a Nodeobject`

        Args:
            data (int): value of the node
            next_node (Node): pointer to the next node object or None
        """

        if type(data) != int:
            raise TypeError("data must be an integer")
        else:
            self.__data = data

        if (type(next_node) != None) or (type(next_node) != Node):
            raise TypeError("next_node must be a Node object")
        else:
            self.__next_node = next_node

    @property
    def data(self):
        """Retrieve the value of the node object

        Returns:
            An integer value
        """

        return self.__data

    @data.setter
    def data(self, value):
        """Set the data value of the node object

        The argument value must be an integer, otherwise raise a TypeError
        with the exception message `data must be an integer`

        Args:
            value (int): value of the node
        """

        if type(value) != int:
            raise TypeError("data must be an integer")
        else:
            self.__data = value

    @property
    def next_node(self):
        """Retrieve the address of the next node object

        Returns:
            The next Node object
        """

        return self.__next_node

    @next_node.setter
    def next_node(self, value):
        """Set the next_node attribute of this object

        The argument `value` must be None or Node object, otherwise it
        raises a TypeError exception with the message
        `next_node must be a Node object`

        Args:
            value (Node): Holds the address of the next node object or None
        """

        if (type(value) != None) or (type(value) != Node):
            raise TypeError("next_node must be a Node object")
        else:
            self.__next_node = value


# end of class Node




    def __init__(self):
        """Initialize a SinglyLinkedList object
        """

        self.__head = None

    def __str__(self):
        """Print the entire list

        Prints the entire list in stdout
        one node number by line
        """

        original_head = Node(self.__head)
        my_str = str()
        while self.__head != None:
            my_str += str(self.__head.data()) + '\n'
            self.__head = self.__head.next_node()
