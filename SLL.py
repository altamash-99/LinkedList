class Node:
    # Class to Create a node object for the SLL
    def __init__(self, data=None, nxt=None):
        self.data = data
        self.nxt = nxt


class SinglyLinkedList:
    def __init__(self):
        self.head = None

    def insert_at_beginning(self, data):
        """
        To insert any data at the beginning of the Linked List.

        insert_at_beginning(data)
        :param data: The data to be inserted at the beginning of the Linked List.
        :return: None
        """
        self.head = Node(data, self.head)
        return

    def insert_at_end(self, data):
        """
        To insert any data at the end of the Linked List.

        insert_at_end(data)
        :param data: The data to be inserted at the end of the Linked List.
        :return: None
        """
        if self.head is None:
            self.head = Node(data, self.head)
            return

        itr = self.head

        while itr.nxt:
            itr = itr.nxt

        itr.nxt = Node(data, None)

    def insert_at(self, pos, data):
        """
        To insert any data at any valid position on the list.
        Raises Exception if the pos value passed is invalid(i.e. Not in the range of indices of SLL).

        :param pos: The position where the data is to be inserted.
        :param data: Data to be inserted.
        :return: None
        """
        if not 0 <= pos < self.get_length():
            raise Exception('Invalid Index!!!')
            return

        if pos == 0:
            self.insert_at_beginning(data)
            return

        itr = self.head
        index = 0

        while index != pos - 1:
            itr = itr.nxt
            index += 1

        node = Node(data, itr.nxt)
        itr.nxt = node

    def insert_values(self, values):
        """
        To insert a list of values directly to SLL.
        Note: It overwrites the previously stored data on the SLL.

        :param values:
        :return:
        """
        self.head = None
        for value in values:
            self.insert_at_end(value)

    def insert_after_value(self, data_after, data_to_insert):
        """
        Insert data after the first occurred data_after(data)

        :param data_after: The existing data on SLL after which a new data (data_to_insert) is to be inserted
        :param data_to_insert: The data to be inserted after (data_after)
        :return: None
        """
        itr = self.head
        index = 0

        while itr.data != data_after:
            itr = itr.nxt
            index += 1
            if itr is None:
                print(f'Node with data {data_after} not present!!!')
                return

        self.insert_at(index + 1, data_to_insert)

    def remove_at_beginning(self):
        # Removes data at the beginning of the SLL

        self.head = self.head.nxt
        return

    def remove_at_end(self):
        # Removes data at the end of the SLL
        itr = self.head

        while itr.nxt.nxt:
            itr = itr.nxt

        itr.nxt = None
        return

    def remove_at(self, pos):
        """
        To remove an element at some position on the SLL.
        Raises Exception if the pos value passed is invalid(i.e. Not in the range of indices of SLL).

        :param pos: The position at which data is to be removed.
        :return: None
        """
        if not 0 <= pos <= self.get_length():
            raise Exception('Invalid Index!!!')
            return

        if pos == 0:
            self.remove_at_beginning()
            return

        elif pos == self.get_length()-1:
            self.remove_at_end()
            return

        itr = self.head
        index = 0

        while index != pos - 1:
            itr = itr.nxt
            index += 1

        itr.nxt = itr.nxt.nxt

    def remove_by_value(self, data):
        """
        Removes the first occurred (data) on SLL

        :param data: The data to be removed from the SLL
        :return: None
        """
        if self.head is None:
            print('Empty SLL')

        itr = self.head
        index = 0

        while itr.data != data:
            itr = itr.nxt
            index += 1

        self.remove_at(index)

    def get_length(self):
        """
        Returns length of the linked list.
        """
        count = 0
        itr = self.head

        while itr:
            count += 1
            itr = itr.nxt

        return count

    def print(self):
        """
        Prints the entire linked list.
        :return: None
        """
        if self.head is None:
            print('Linked List is Empty!')
            return

        itr = self.head
        llstr = ''

        while itr:
            llstr += str(itr.data) + '-->' if itr.nxt else str(itr.data)
            itr = itr.nxt
        print()
        print(llstr)

    def print_nodes(self):
        """
        Prints the entire SLL in form of its Nodes

        :return: None
        """

        if self.head is None:
            print('SLL is empty!')
            return

        itr = self.head
        llstr = ''

        while itr:
            llstr += f'|{itr.data}|{hex(id(itr.nxt))}|-->' if itr.nxt else f'|{itr.data}|{None}|'
            itr = itr.nxt

        print()
        print(f'|{hex(id(self.head))}|')
        print(' |')
        print(' V')
        print(llstr)