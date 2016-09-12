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
		for i in range(self.width):
			self.part[3][i] = 1
	def down(self):
		for j in range(4):
			if self.part[self.object[j][0]][self.object[j][1]+1] == 1:
				return 0
		for j in range(4):
			self.object[j][1]+=1
		return 1
	def line(self):
		for j in range(self.height):
			l = 1
			for i in range(self.width):
				if self.part[j][i] == 0:
					l=0
			if l==1:
				self.part.pop(j)
				self.part.insert(0, [0]*self.width)
			



F = Field(10, 10)

print_field(F.part, F.object)
#d = F.down()
F.line()
print_field(F.part, F.object)