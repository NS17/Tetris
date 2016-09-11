# here will be the logic of the program
# here will be the logic of the program

 from graphics import print_field
 
class Field:
	def __init__(self, height, width):
		self.part  = [[0] * width for i in range(height)]
		self.object = [(0,0), (0,1), (0,2), (1,1)]
		self.part[1][1] = self.part[1][2] = 1

F = Field(5, 5)
#F[]
print_field(F.part, F.object)

#print(F.object)
print('Hi')