nums = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]
def deletetailnode(head):
    if head == none or head.next==none:
        return none

    previous = none
    currentnode = head

    while currentnode.next !=none:
        previos = currentnode
        currentnode = currentnode.next

    previous.next = none
    return head
