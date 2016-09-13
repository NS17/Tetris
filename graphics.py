import os

def print_field(self):
    # os.system('cls')
    for y, row in enumerate(self.part):
        s = ''
        for x, val in enumerate(row):
            if val or [x,y] in self.object:
                s += '#'
            else:
                s += ' '
        print(s)