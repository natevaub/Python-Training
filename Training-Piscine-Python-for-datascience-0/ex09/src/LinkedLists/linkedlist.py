class Node:
    def __init__(self, data=None, next=None):
        """
        Initializes a new node with given data and reference to the next node.
        """
        self.data = data
        self.next = next

class LinkedList:
    def __init__(self):
        """
        Initializes an empty linked list.
        """
        self.head = None

    def insert_at_beginning(self, data):
        """
        Inserts a new node with the specified data at the beginning of the list.
        """
        node = Node(data, self.head)
        self.head = node

    def print(self):
        """
        Prints the linked list in a readable format.
        """
        if self.head is None:
            print('LinkedList empty')
            return
        
        itr = self.head
        llstr = ''
        while itr:
            llstr += str(itr.data) + '---> '
            itr = itr.next

        print(llstr)

    def insert_at_end(self, data):
        """
        Inserts a new node with the specified data at the end of the list.
        """
        if self.head is None:
            self.head = Node(data, None)
            return
        
        itr = self.head
        while itr.next:
            itr = itr.next

        itr.next = Node(data, None)

    def insert_values(self, data_list):
        """
        Inserts multiple values into the linked list from the provided list.
        Reinitializes the linked list.
        """
        self.head = None 
        for data in data_list:
            self.insert_at_end(data)

    def get_length(self):
        """
        Returns the number of nodes in the linked list.
        """
        count = 0
        itr = self.head
        while itr:
            count += 1
            itr = itr.next
        return count

    def remove_at(self, index):
        """
        Removes the node at the specified index.
        Raises an exception if the index is invalid.
        """
        if index < 0 or index >= self.get_length():
            raise Exception('Invalid index')

        if index == 0:
            self.head = self.head.next 
            return

        count = 0
        itr = self.head
        while itr:
            if count == index - 1:
                itr.next = itr.next.next
                break
            itr = itr.next
            count += 1

    def insert_at(self, index, data):
        """
        Inserts a new node with the specified data at the given index.
        Raises an exception if the index is invalid.
        """
        if index < 0 or index > self.get_length():
            raise Exception("Invalid index")

        if index == 0:
            self.insert_at_beginning(data)
            return

        if index == self.get_length():
            self.insert_at_end(data)
            return

        count = 0
        itr = self.head
        while itr:
            if count == index - 1:
                node = Node(data, itr.next)
                itr.next = node
                break
            itr = itr.next
            count += 1

    def insert_after_value(self, data_after, data_value):
        """
        Inserts a new node with 'data_value' after the first node with 'data_after'.
        """
        itr = self.head
        while itr:
            if itr.data == data_after:
                new_node = Node(data_value, itr.next)
                itr.next = new_node
                return
            itr = itr.next

    def remove_by_value(self, data_value):
        """
        Removes the first occurrence of a node that contains the specified data.
        Does nothing if the list is empty or the value is not found.
        """
        if not self.head:
            return
        
        if self.head.data == data_value:
            self.head = self.head.next
            return

        itr = self.head
        while itr.next:
            if itr.next.data == data_value:
                itr.next = itr.next.next
                return
            itr = itr.next