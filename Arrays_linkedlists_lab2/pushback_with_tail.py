def pushback_with_tail(self, info):
    node=Node(data)
    if self.head==None:
        self.head=self.tail=node
    else:
        self.tail.next=node
        self.tail= node
    
        