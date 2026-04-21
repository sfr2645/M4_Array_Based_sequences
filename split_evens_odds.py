from singly_linked_list import SinglyLinkedList, Node

class SplitEvensOdds(SinglyLinkedList):
    def split(self):
        evens = SinglyLinkedList()
        odds = SinglyLinkedList()

        even_tail = None
        odd_tail = None
        current = self.head

        while current:
            next_node = current.next
            current.next = None

            if current.data % 2 == 0:
                if evens.head is None:
                    evens.head = current
                    even_tail = current
                else:
                    even_tail.next = current
                    even_tail = current
            else:
                if odds.head is None:
                    odds.head = current
                    odd_tail = current
                else:
                    odd_tail.next = current
                    odd_tail = current

            current = next_node

        self.head = None
        return evens, odds