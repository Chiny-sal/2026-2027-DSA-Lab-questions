a=[1,2]
b=[a,a]
b[0].append(3)
print(b)

def getiteam(self,k):
    if self._n<k:
        raise IndexError("invalid index")
    cur=self.head
    for i in range(k-1):
        cur=cur.next
    return cur.data


def count_nodes(self,node):
    if node.next==None:
        return 1
    else:
        return count_nodes(node.right)+ count_nodes(node.left)+1
