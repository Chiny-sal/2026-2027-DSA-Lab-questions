def middle(self):
    slow=fast=self.header
    while fast!=None and fast.next !=None:
        fast=fast.next.next
        slow=slow.next
    return slow.data
