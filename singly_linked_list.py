class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class SinglyLinkedList:
    def __init__(self):
        self.head = None

    def build_list_forward(self, values):
        for value in values:
            new_node = Node(value)
            if self.head is None:
                self.head = new_node
            else:
                current = self.head
                while current.next:
                    current = current.next
                current.next = new_node

    def build_list_backward(self, values):
        for value in values:
            new_node = Node(value)
            new_node.next = self.head
            self.head = new_node

    def display(self):
        current = self.head
        result = "Head -> "
        while current:
            result += str(current.data) + " -> "
            current = current.next
        result += "None"
        print(result)

    def delete_first(self):
        if self.head:
            self.head = self.head.next

    def delete_last(self):
        if self.head is None:
            return
        if self.head.next is None:
            self.head = None
            return

        current = self.head
        while current.next.next:
            current = current.next
        current.next = None

    def delete_value(self, value):
        if self.head is None:
            return

        if self.head.data == value:
            self.head = self.head.next
            return

        current = self.head
        while current.next:
            if current.next.data == value:
                current.next = current.next.next
                return
            current = current.next

    def remove_all(self, value):
        while self.head and self.head.data == value:
            self.head = self.head.next

        current = self.head
        while current and current.next:
            if current.next.data == value:
                current.next = current.next.next
            else:
                current = current.next

    def display_reverse_nr(self):
        stack = []
        current = self.head

        while current:
            stack.append(current.data)
            current = current.next

        result = "None <- "
        while stack:
            result += str(stack.pop()) + " <- "
        result += "Head"
        print(result)
