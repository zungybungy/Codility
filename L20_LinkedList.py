class Node:
    def __init__(self, initdata):
        self.data = initdata
        self.next = None
        self.prev = None  # only if doubly linked

    def getData(self):
        return self.data

    def getNext(self):
        return self.next

    def setData(self, newdata):
        self.data = newdata

    def setNext(self, newnext):
        self.next = newnext


class LinkedList(object):
    def __init__(self, head=None):
        self.head = head


    def isEmpty(self):
        return self.head == None


    def insert(self, data):
        new_node = Node(data)
        new_node.set_next(self.head)
        self.head = new_node


    def size(self):
        current = self.head
        count = 0
        while current:
            count += 1
            current = current.get_next()
        return count


    def search(self, data):
        current = self.head
        found = False
        while current and found is False:
            if current.get_data() == data:
                found = True
            else:
                current = current.get_next()
        if current is None:
            raise ValueError("Data not in list")
        return current


    def delete(self, data):
        current = self.head
        previous = None
        found = False
        while current and found is False:
            if current.get_data() == data:
                found = True
            else:
                previous = current
                current = current.get_next()
        if current is None:
            raise ValueError("Data not in list")
        if previous is None:
            self.head = current.get_next()
        else:
            previous.set_next(current.get_next())


    #Reverse inkedlist
    def reverse_list(head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if not head or not head.next:
            return head
        prev = None
        while head:
            current = head
            head = head.next
            current.next = prev
            prev = current
        return prev