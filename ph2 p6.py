def insertatspecificposition(head,position,ele):
    if position == 0:
        return insertathead(head,ele)
    temp=node(ele)
    index=0
    currentnode=head
    while index != position - 1:
        currentNode = currentNode.next 
        index += 1 
 
    nextNode = currentNode.next 
    temp.next = nextNode 
    currentNode.next = temp 
    return head
 
    
