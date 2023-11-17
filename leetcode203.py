# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def print_lst(head):
    current = head
    while current.next:
        print(current.val)
        current = current.next
    print(current.val)


head = ListNode(1)
for i in [2,6,3,4,5,6]:
    current = head
    while current.next:
        current = current.next
    current.next = ListNode(i)

print_lst(head)
def removeElements(head, val):
    fix_head = ListNode(next=head)
    current = fix_head

    while current.next:

        if current.next.val == val:
            current.next = current.next.next
        else:
            current = current.next
    return fix_head.next
print('\n')
print_lst(removeElements(head, 6))        


