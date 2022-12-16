class Vector:
   
	def __init__(self,  x, y, z):
		self.x = x
		self.y = y
		self.z = z

	def show(self):
		print(self.x,",", self.y,",",self.z)
	
	
	def __add__(self, otherVector):
		newVectorX = self.x + otherVector.x
		newVectorY = self.y + otherVector.y
		newVectorZ = self.z + otherVector.z
		return Vector(newVectorX, newVectorY, newVectorZ)


	def resta(self, otherVector):
		newVectorX = self.x - otherVector.x
		newVectorY = self.y - otherVector.y
		newVectorZ = self.z - otherVector.z
		return Vector(newVectorX, newVectorY, newVectorZ)

	def pro_escalar(self, otherVector):
		escalar = self.x*otherVector.x + self.y*otherVector.y +self.z*otherVector.z
		return escalar

	def pro_vectorial(self, otherVector):
		newVectorX = (self.y*otherVector.z -self.z*otherVector.y)
		newVectorY = -(self.x*otherVector.z - self.z*otherVector.x)
		newVectorZ = (self.x*otherVector.y - self.y*otherVector.x)
		return Vector(newVectorX, newVectorY, newVectorZ)


x = input("Ingrese x: ")
y = input("Ingrese y: ")
z = input("Ingrese z: ")
v1 = Vector(x, y, z)
x2 = input("Ingrese x2: ")
y2 = input("Ingrese y2: ")
z2 = input("Ingrese z2: ")
v2 = Vector(x2, y2, z2)
