def reverse_list(self,data):
    link_to= None
    now=self.head
    while now != None:
        Inline= now.next
        now.next=link_to
        link_to=now
        now=Inline
    self.head=link_to




