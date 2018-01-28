#Define a class that has two properties x and y. Add a method to the class that adds x & y.
#Write a routine that uses this class to add two numbers. Write some test cases to test the
#addition method in the class


class Sampletest:
	def __init__(self,a,b):
		self.a = a
		self.b = b

	@property
	def prop_a(self):
		return self.a

	@property
	def prop_b(self):
		return self.b

	def add(self):
		return self.a + self.b

ob=Sampletest(3,5)
print(ob.add())