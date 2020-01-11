from doubly_linked_list import DoublyLinkedList
class RingBuffer:
    def __init__(self, capacity):
        self.capacity = capacity
        self.current = None #where the head of our ring is
        self.storage = DoublyLinkedList()
    def append(self, item):
        #initiate the ring
        if self.storage.length == 0:
            self.storage.add_to_head(item)
            self.current = self.storage.head
        #if at capacity and current isn't at head, remove from head, add to tail
        elif self.storage.length == self.capacity and not self.current is self.storage.head:
            self.storage.remove_from_head()
            self.storage.add_to_tail(item)
        #if at capacity and current is at the head; move current to tail
        elif self.storage.length == self.capacity:
            self.storage.remove_from_head()
            self.storage.add_to_tail(item)
            self.current = self.storage.tail
        #if not at capacity; add to tail
        else:
            self.storage.add_to_tail(item)
    def get(self):
        # Note:  This is the only [] allowed
        list_buffer_contents = []
        while len(list_buffer_contents) < self.storage.length:
            list_buffer_contents.append(self.current.value)
            if self.current.next: self.current = self.current.next
            else: self.current = self.storage.head
        return list_buffer_contents
# ----------------Stretch Goal-------------------


class ArrayRingBuffer:
    def __init__(self, capacity):
        pass

    def append(self, item):
        pass

    def get(self):
        pass
