class Node:
    def __init__(self, val = 0, next = None) -> None:
        self.val = val
        self.next = next

class MyLinkedList:

    def __init__(self):
        self.head = Node()
        self.size = 0

    def get(self, index: int) -> int:
        if index < 0 or index > self.size - 1:
            return -1
        current_head = self.head
        current_index = 0
        while current_head.next and current_index < index:
            current_head = current_head.next
            current_index += 1
        print(f'current cal = {current_head.next.val}')
        return current_head.next.val

    def addAtHead(self, val: int) -> None:
        current = Node(val)
        current.next = self.head.next
        self.head.next = current
        self.size += 1

    def addAtTail(self, val: int) -> None:
        current = Node(val)
        current_head = self.head
        while current_head.next:
            current_head = current_head.next
        current_head.next = current
        self.size += 1

    def addAtIndex(self, index: int, val: int) -> None:
        if index < 0 or index > self.size:
            return  
        current = Node(val)
        current_head = self.head
        current_index = 0
        while current_head.next and current_index < index:
            current_head = current_head.next
            current_index += 1
        current.next = current_head.next
        current_head.next = current
        self.size += 1

    def deleteAtIndex(self, index: int) -> None:
        if index < 0 or index > self.size - 1:
            return 
        current_head = self.head
        # print(self.head.__dict__)
        # print(current_head.__dict__)
        # print(current_head  ==  self.head)
        current_index = 0
        while current_head.next and current_index < index:
            current_head = current_head.next
            current_index += 1
        current_head.next = current_head.next.next
        self.size -= 1


    def print_lst(self):
        current = self.head
        while current.next:
            print(current.val)
            current = current.next
        print(current.val)

            

# Your MyLinkedList object will be instantiated and called as such:
obj = MyLinkedList()
# param_1 = obj.get(index)
obj.addAtHead(1)
# obj.get(1)
# obj.deleteAtIndex(1)
obj.addAtTail(3)
obj.addAtIndex(1,2)
obj.print_lst()
print('.........')
print(obj.get(1))
obj.deleteAtIndex(1)
print(obj.get(1))
obj.print_lst()

# obj.addAtIndex(0,10)
# obj.addAtIndex(0,20)

# obj.addAtIndex(1,30)
# obj.deleteAtIndex(1)

# obj.print_lst()
# print('........')
# # obj.print_lst()
# obj.get(0)