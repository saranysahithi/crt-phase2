def insertAtSpecificPosition(head, position, ele):
    if position == 0:
        return insertAtHead(head, ele)
 
def deleteheadnode(head):
    if head == none:
        return head
    secondnode = head.next
    head.next = none
    return secondnode
nums = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]
head = None 
for ele in nums:
    head = insertAtTail(head, ele)
print("Final linked list is:")
printLinkedList(head)
