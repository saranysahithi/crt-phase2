class node():
    def __init__(self,data):
        self.data = data
        self.next = none
obj1= node(71)
obj2= node(72)
obj3= node(73)
obj4= node(74)
obj5= nofe(75)
obj6= node(76)
obj7= node(77)
obj8= node(78)
obj9= node(79)
obj10= node(80)
obj1.next=obj2
obj2.next=obj3
obj3.next=obj4
obj4.next=obj5
obj5.next=obj6
obj6.next=obj7
obj7.next=obj8
obj8.next=obj9
obj9.next=obj10
currentnode=obj1
while currentnode!=none:
    print(currentnode.data,end='-->')
    currentnode=currentnode.next
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
