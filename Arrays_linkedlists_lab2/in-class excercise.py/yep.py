
def getiteam(self,k):
    if self._n<k:
        raise IndexError("invalid index")
    cur=self.head
    for i in range(k-1):
        cur=cur.