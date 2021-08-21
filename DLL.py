class Node:
    # Class to Create a node object for the DLL
    def __init__(self, prev=None, data=0, nxt=None):
        self.prev = prev
        self.data = data
        self.nxt = nxt


class DoublyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def get_length(self):
        # Returns the length of the DLL
        length = 0

        itr = self.head

        while itr:
            length += 1
            itr = itr.nxt

        return length

    def display_forward(self):
        """
        Displays the entire DLL in forward direction

        :return: None
        """
        itr = self.head

        llstr = ''
        while itr:
            llstr += str(itr.data) + '-->' if itr.nxt else str(itr.data)
            itr = itr.nxt
        print(llstr)
        return

    def display_backward(self):
        """
        Displays the entire DLL in backward direction

        :return: None
        """
        itr = self.tail

        llstr = ''
        while itr:
            llstr += str(itr.data) + '-->' if itr.prev else str(itr.data)
            itr = itr.prev
        print(llstr)
        return

    def display_nodes(self):
        """
        Displays the entire DLL in form of its Nodes

        :return: None
        """
        itr = self.head

        llstr = ''

        while itr:
            if itr.prev is None:
                llstr += f'|{None}| {itr.data} |{hex(id(itr.nxt))}|' + '<-->'

            elif itr.nxt is not None:
                llstr += f'|{hex(id(itr.prev))}| {itr.data} |{hex(id(itr.nxt))}|' + '<-->'

            else:
                llstr += f'|{hex(id(itr.prev))}| {itr.data} |{None}| '

            itr = itr.nxt

        print()
        print(f'|{hex(id(self.head))}|')
        print(' |')
        print(' V')
        print(llstr)
        return

    def insert_at_beginning(self, data):
        """
        Inserts data at the beginning of the DLL

        :param data: data to be inserted
        :return: None
        """
        if self.head is None:
            self.head = Node(None, data, None)
            self.tail = self.head
            return

        self.head = Node(None, data, self.head)
        self.head.nxt.prev = self.head
        return

    def insert_at_end(self, data):
        """
        Inserts data at the end of the DLL

        :param data: data to be inserted
        :return: None
        """
        if self.head is None:
            self.head = Node(None, data, None)
            self.tail = self.head
            return

        node = Node(self.tail, data, None)
        self.tail.nxt = node
        self.tail = node
        return

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

        for i in range(1, pos):
            itr = itr.nxt

        node = Node(itr, data, itr.nxt)
        itr.nxt.prev = node
        itr.nxt = node
        return

    def insert_after(self, data_after, data):
        """
        Inserts a data value after the first occurred passed data(data_after)

        :param data_after: The data after which a new data is to be inserted
        :param data: The data to be inserted
        :return: None
        """
        itr = self.head

        while itr.data != data_after:
            itr = itr.nxt
            if itr is None:
                # Will be executed when itr = None and there is no data matched to data_after i.e. at the end of the DLL
                print(f'Node with data {data_after} not present!!!\n')
                return

        if itr.nxt is None:
            self.insert_at_end(data)
            return

        node = Node(itr, data, itr.nxt)
        itr.nxt.prev = node
        itr.nxt = node
        return

    def insert_values(self, values):
        """
        Insert the data stored in the passed list(values)
        Data is inserted in same order that it is present in the passed list(values)
        Note: It overwrites the previously stored data in DLL

        :param values: Contains the data to be inserted
        :return: None
        """
        self.head = None
        self.tail = None
        for value in values:
            self.insert_at_end(value)
        return

    def remove_at_beginning(self):
        # Removes data at the beginning of the DLL

        self.head = self.head.nxt
        self.head.prev = None
        return

    def remove_at_end(self):
        # Removes data at the end of the DLL
        self.tail = self.tail.prev
        self.tail.nxt = None
        return

    def remove_at(self, pos):
        """
        Removes data at the desired position
        Raises Exception if the pos value passed is invalid(i.e. Not in the range of indices of DLL).

        :param pos: position at which data is to be removed
        :return: None
        """
        if not 0 <= pos < self.get_length():
            raise Exception('Invalid Index!!!')
            return

        itr = self.head

        if pos == 0:
            self.remove_at_beginning()
            return

        elif pos == self.get_length() - 1:
            self.remove_at_end()
            return

        index = 0
        while index != pos-1:
            itr = itr.nxt
            index += 1

        node = itr.nxt.nxt

        node.prev = itr
        itr.nxt = node
        return

    def remove_by_value(self, data):
        """
        Removes the first occurred (data) on DLL

        :param data: The data to be removed from the DLL
        :return: None
        """
        itr = self.head

        while itr.nxt.data != data:
            itr = itr.nxt
            if itr is None:
                print('The passed value doesn\'t exist')
                return

        node = itr.nxt.nxt

        node.prev = itr
        itr.nxt = node
        return