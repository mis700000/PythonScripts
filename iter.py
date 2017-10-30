def xyzrange():
    def__init(self,n):
	    self.i = 0
		self.n = n
	def__iter__(self):
	    return self
	def next(self):
	    if self.i<self.n:
		    i = self.i
			self.i += 1
			return i
		else:
		    raise StopIteration()
xyz=xyzrange(3)
print(xyz.next())
print(xyz.next())
print(xyz.next())