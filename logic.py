# here will be the logic of the program
# here will be the logic of the program
from graphics import print_field
 
class Field:
	def __init__(self, height, width):
		self.width = width
		self.height = height
		self.part  = [[0] * width for i in range(height)]
		self.object = [[0,0], [0,1], [0,2], [1,1]]
		self.part[1][1] = self.part[1][2] = 0
		#for i in range(self.width):
			#self.part[3][i] = 1
	def down(self):
		for x, y in self.object:
			if self.part[x][y+1] == 1:
				return False
		for j in range(len(self.object)):
			self.object[j][1]+=1
		return True
	def left(self):
		for x, y in self.object:
			if self.part[x+1][y] == 1 or x==0:
				return 
		for j in range(len(self.object)):
			self.object[j][0]-=1

	def right(self):
		for x, y in self.object:
			if self.part[x+1][y] == 1 or x==self.width:
				return 
		for j in range(len(self.object)):
			self.object[j][0]+=1
		
	def line(self):
		lines = 0
		new_field = []
		for row in self.part:
			if sum(row) == self.width:
				lines += 1
			else:
				new_field.append(row)
		self.part = new_field + [[0] * self.width for x in range(lines)]
		return lines

	def place_object(self):
		print(self.object)
		for x, y in self.object:
			self.part[x][y] = 1
		self.object = [[0,0], [0,1], [0,2], [1,1]]

			



F = Field(10, 10)

#print_field(F.part, F.object)
d = F.down()
l = F.line()
r = F.right()
r = F.right()
r = F.right()
r = F.right()
print(l)
#print_field(F.part, F.object)
F.place_object()
#print_field(F.part, F.object)
