def deletenodeatspecificposition(head,position):
    index=0
    currentnode=head
    while index !=position-1:
        index+= 1
        currentnode=currentnode.next
    nodetobedeleted = currentnode.next
    nextnode = nodetobedeleted.next

    nodetobedeleted.next = none
    currentnode.next= none
    currentnode.next = nextnode
    
