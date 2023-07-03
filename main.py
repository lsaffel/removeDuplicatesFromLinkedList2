class LinkedList:
    def __init__(self, value):
        self.value = value
        self.next = None


def removeDuplicatesFromLinkedList(linkedList):
    a = linkedList
    b = a.next

    while b != None:
        # advance both pointers until the values are different
        while b != None and a.value == b.value:
            b = b.next

        # check if the end of the list has been found or not
        if b != None:
            if a.value == b.value:
                a.next = None
            else:
                a.next = b
                a = b
                b = b.next

        # b is pointing past the end of the list, so the values are the same. 
        # Therefore, the last node is a duplicate, so point a at None, 
        # to remove the last duplicate node.
        else:
            a.next = None
    return linkedList
