#!/usr/bin/python3
"""This module implements a singly linked list ADT

Attributes:
    Node (class): represents a node object
    SinglyLinkedList (class): represents a list object
"""


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

        if (next_node is None) or (type(next_node) == Node):
            self.__next_node = next_node
        else:
            raise TypeError("next_node must be a Node object")

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

        if not isinstance(value, int):
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

        if (value is not None) and not isinstance(value, Node):
            raise TypeError("next_node must be a Node object")
        else:
            self.__next_node = value


class SinglyLinkedList:
    """Represent a singly linked list object

    Attributes:
        Node (class): represents a node object
        __head (Node): head of the list
    """

    def __init__(self):
        """Initialize a SinglyLinkedList object
        """

        self.__head = None

    def __str__(self):
        """Convert a SinglyLinkedList to string format

        Returns:
            The entire list in str format, one node number by line
            Or an empty line if linked list is empty
        """

        tmp = Node(self.__head.data)
        tmp.next_node = self.__head.next_node

        values = []
        while tmp is not None:
            values.append(tmp.data)
            tmp = tmp.next_node
        
        values = [str(var) for var in values]
        return ('\n'.join(values))

    def sorted_insert(self, value):
        """Insert a new Node object

        Inserts a new Node object into the correct sorted position
        in the list (increasing order)

        Args:
            value (int): value to be held by the Node object
        """

        if type(value) != int:
            raise TypeError("data must be an integer")

        new = Node(value, None)

        # empty list
        if self.__head is None:
            print('self.__head is {}'.format(self.__head))   # test
            self.__head = new
            print('Therefore, self.__head should point to {}'.format(self.__head)) # test
        else:
            # Find comfortable position
            print('\nFinding comfortable position\n')  # test
            tmp = Node(self.__head.data)
            tmp.next_node = self.__head.next_node
            print('tmp is {}'.format(tmp))
            print('tmp.next_node is {}'.format(tmp.next_node)) # test
            print('tmp.data is {:d}'.format(tmp.data))  # test
            while tmp is not None:
                print('\ntmp is {}\n'.format(tmp))  # test
                if tmp.data <= new.data:
                    print('\ntmp is <= new.data\n')  # test
                    if tmp.next_node is None:
                        print('\ntmp  is {}\n'.format(tmp)) # test
                        tmp.next_node = new
                        print('Therefore, tmp should point to {}\n'.format(tmp.next_node))
                        break
                    if tmp.next_node.data >= new.data:
                        new.next_node = tmp.next_node
                        tmp.next_node = new
                        break
            

        # test test test
        print('self.__head is {}'.format(self.__head)) # test
        print('self.__head.data is {:d}'.format(self.__head.data))  # test
        print('self.__head.next_node is {}'.format(self.__head.next_node))  # test
