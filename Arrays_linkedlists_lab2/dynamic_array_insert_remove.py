def insert_value(self, k, x):
    if not 0<=k <self._n:
        raise IndexError("index out of bounds")
    if self._n==self.cap:
        self.resize(2*self.cap)
    for i in range(self._n, k, -1):
        self.data[i]=self.data[i-1]
    self.data[k]=x
    self._n+=1
def remove_by_index(self,k):
    if not 0<=k< self._n:
        raise IndexError("index out of bounds")
    for i in range(k,self._n-1):
        self.data[i]=self.data[i+1]
    self.data[self._n-1]=None
    self._n-=1
    