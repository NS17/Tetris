# here will be the logic of the program
# here will be the logic of the program
from graphics import print_field
import msvcrt
import time
import math

class Field:
	def __init__(self, height, width):
		self.width = width
		self.height = height
		self.part  = [[0] * width for i in range(height)]
		self.object = [[0,0], [1,0], [2,0], [1,1]]
		self.part[1][1] = self.part[1][2] = 0
		#for i in range(self.width):
			#self.part[3][i] = 1
	def down(self):
		for x, y in self.object:
			if y==self.height-1  or self.part[y+1][x]==1:
				return False
		for j in range(len(self.object)):
			self.object[j][1]+=1
		return True
	def left(self):
		for x, y in self.object:
			if x==0 or self.part[y][x-1] == 1:
				return 
		for j in range(len(self.object)):
			self.object[j][0]-=1

	def right(self):
		for x, y in self.object:
			if x==self.width-1 or self.part[y][x+1] == 1 :
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
		for x, y in self.object:
			self.part[y][x] = 1
		self.object = [[0,0], [1,0], [2,0], [1,1]]

	def new_object(self):
		while self.check(): 
			while self.down():
				was = time.clock()
				print_field(self)
				while(math.fabs(time.clock()-was) < 0.5):
					if msvcrt.kbhit():
						var = msvcrt.getch()
						if var == b'a':
							self.left()
							#print_field(self)
						if var == b'd':
							self.right()
							#print_field(self)
			self.place_object()
		print_field(self)

	def check(self):
		for x, y in self.object:
			if self.part[y][x] == 1: return False
		return True

F = Field(10, 10)
F.down()
print_field(F)

F.new_object()
#for i in range(len(F.part)):
#	for j in range(len(F.part[i])):
#		print(i, j, F.part[j][i])
#d = F.down()
#l = F.line()
#r = F.right()
#r = F.left()
#print_field(F)
#print_field(F)
#F.place_object()
#print_field(F)
