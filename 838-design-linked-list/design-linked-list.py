class MyLinkedList:

    def __init__(self):
        self.dummy=ListNode(0)
        self.size=0
        

    def get(self, index: int) -> int:
        if index < 0 or index >= self.size:
            return -1

        curr = self.dummy.next

        for _ in range(index):
            curr = curr.next

        return curr.val
        

    def addAtHead(self, val: int) -> None:
        newNode=ListNode(val)
        newNode.next = self.dummy.next
        self.dummy.next = newNode
        self.size+=1

    def addAtTail(self, val: int) -> None:
        newNode=ListNode(val)
        curr=self.dummy
        while curr.next:
            curr=curr.next

        newNode.next=curr.next
        curr.next=newNode
        self.size+=1
        

    def addAtIndex(self, index: int, val: int) -> None:
        if index < 0 or index > self.size:
            return

        curr = self.dummy

        for _ in range(index):
            curr = curr.next

        newNode = ListNode(val)

        newNode.next = curr.next
        curr.next = newNode

        self.size += 1
        

    def deleteAtIndex(self, index: int) -> None:
        if index < 0 or index >= self.size:
            return

        curr = self.dummy

        for _ in range(index):
            curr = curr.next

        curr.next = curr.next.next

        self.size -= 1
        


# Your MyLinkedList object will be instantiated and called as such:
# obj = MyLinkedList()
# param_1 = obj.get(index)
# obj.addAtHead(val)
# obj.addAtTail(val)
# obj.addAtIndex(index,val)
# obj.deleteAtIndex(index)