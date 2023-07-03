class LinkedList:
    def __init__(self, value):
        self.value = value
        self.next = None


def removeDuplicatesFromLinkedList(linkedList):
    a = linkedList
    b = a.next

    while b != None:
        while b != None and a.value == b.value:
            b = b.next

        if b != None:
            if a.value == b.value:
                a.next = None
            else:
                a.next = b
                a = b
                b = b.next
        else:
            a.next = None
    return linkedList
