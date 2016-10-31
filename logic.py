# here will be the logic of the program
# here will be the logic of the program
from graphics import print_field
import msvcrt
import time
import math
import random

objects = [[[0,0], [1,0], [2,0], [1,1]], [[0,0], [0,1], [0,2]], [[0,0], [0,1], [1,1], [1,2]]]

class Field:
	def __init__(self, height, width):
		self.width = width
		self.height = height
		self.part  = [[0] * width for i in range(height)]
		self.object = self.get_object()
		self.next_object = self.get_object()
		self.object_center = 1
		self.speed = 0.5
		self.score = 0
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

	def switch(self, c, d):
		for x, y in self.object:
			if y+c > self.width-1 or y+c < 0 or -x+d > self.height-1 or -x+d < 0 or self.part[-x+d][y+c] == 1:
				return 
		for j in range(len(self.object)):
			k = self.object[j][0]
			self.object[j][0]=self.object[j][1]+c
			self.object[j][1] =-k+d


	def turn(self):
		c = self.object[self.object_center][0] - self.object[self.object_center][1]
		d = self.object[self.object_center][0] + self.object[self.object_center][1]
		self.switch(c,d)

	def line(self):
		lines = 0
		new_field = []
		for row in self.part:
			if sum(row) == self.width:
				lines += 1
				self.score+=1
				if self.score == 20:
					self.speed-=0.1
					self.score = 0
			else:
				new_field.append(row)
		self.part = [[0] * self.width for x in range(lines)] + new_field
		return lines

	def place_object(self):
		for x, y in self.object:
			self.part[y][x] = 1
		self.object = self.next_object
		self.next_object = self.get_object()
		
	def  get_object(self):
		global objects 
		r = random.randint(0,len(objects)-1)
		objects = [[[0,0], [1,0], [2,0], [1,1]], [[0,0], [0,1], [0,2]], [[0,0], [0,1], [1,1], [1,2]]] 
		return objects[r]

			
	def new_object(self):
		while self.check(): 
			while self.down():
				was = time.clock()
				print_field(self)
				while(math.fabs(time.clock()-was) < self.speed):
					self.line()
					if msvcrt.kbhit():
						var = msvcrt.getch()
						if var == b'a':
							self.left()
						if var == b'd':
							self.right()
						if var == b'w':
							self.turn()
			self.place_object()
		print_field(self)

	def check(self):
		for x, y in self.object:
			if self.part[y][x] == 1: return False
		return True

F = Field(9, 9)
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
