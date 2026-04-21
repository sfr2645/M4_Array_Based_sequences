from singly_linked_list import SinglyLinkedList
from split_evens_odds import SplitEvensOdds

def main():
    print("---- Build a forward list ----")
    sll = SinglyLinkedList()
    sll.build_list_forward([10, 20, 30, 40, 50])
    sll.display()

    sll.delete_first()
    print("Delete the first node:", end=" ")
    sll.display()

    sll.delete_last()
    print("Delete the last node:", end=" ")
    sll.display()

    sll.delete_value(30)
    print("Delete the interior node:", end=" ")
    sll.display()

    print("---- Build a backward list ----")
    sll = SinglyLinkedList()
    sll.build_list_backward([10, 20, 30, 40, 50])
    sll.display()

    sll.delete_first()
    print("Delete the first node:", end=" ")
    sll.display()

    sll.delete_last()
    print("Delete the last node:", end=" ")
    sll.display()

    sll.delete_value(30)
    print("Delete the interior node:", end=" ")
    sll.display()

    print("---- Non-recursive reverse print test----")
    sll = SinglyLinkedList()
    sll.build_list_forward([10, 20, 30, 40, 50])
    print("Insertion order:", end=" ")
    sll.display()
    print("Reverse order (non-recursive):")
    sll.display_reverse_nr()

    print("---- Remove all test ----")
    sll = SinglyLinkedList()
    sll.build_list_forward([1, 2, 4, 6, 1, 3, 6])
    sll.display()

    print("Removing 1 and all duplicates:", end=" ")
    sll.remove_all(1)
    sll.display()

    print("Removing 6 and all duplicates:", end=" ")
    sll.remove_all(6)
    sll.display()

    print("---- Split Evens Odds ----")
    split_list = SplitEvensOdds()
    split_list.build_list_forward([1,2,3,4,5,6,7,8,15,14,13,12,11,10,9])
    split_list.display()

    evens, odds = split_list.split()
    evens.display()
    odds.display()
    split_list.display()


if __name__ == "__main__":
    main()
