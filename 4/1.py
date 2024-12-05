import re
from termcolor import colored


#f = open('input_test1','r')
#f = open('input_test2','r')
f = open('input','r')

xmas = 0
grid = []
marked = []

def print_grid(grid,marked):
   # print the characters marked as part of a detected word in different color
   color = 'red'
   for y in range(len(grid)):
      for x in range(len(grid[0])):
         if (x,y) in marked:
            print(colored(grid[y][x], color),end=' ')
         else:
            print(grid[y][x],end=' ')
      print()

def nextc(coord, direction):
   nc = [-1,-1]

   if direction == '>':
      nc[0] = coord[0]
      nc[1] = coord[1] + 1
   elif direction == '<':
      nc[0] = coord[0]
      nc[1] = coord[1] - 1
   elif direction == 'v':
      nc[0] = coord[0] + 1
      nc[1] = coord[1]
   elif direction == '^':
      nc[0] = coord[0] - 1
      nc[1] = coord[1]
   elif direction == 'd>v':
      nc[0] = coord[0] + 1
      nc[1] = coord[1] + 1
   elif direction == 'd>^':
      nc[0] = coord[0] - 1
      nc[1] = coord[1] + 1
   elif direction == 'd<v':
      nc[0] = coord[0] + 1
      nc[1] = coord[1] - 1
   elif direction == 'd<^':
      nc[0] = coord[0] - 1
      nc[1] = coord[1] - 1
      
   return nc

def in_grid(coord,grid):
    if coord[0] < 0 or coord[0] >= len(grid):
        return False
    if coord[1] < 0 or coord[1] >= len(grid[0]):
        return False
    return True
    
def check_path(coord,grid,direction):
   marks = []

   #print("debug: check_path from",coord[0],coord[1], " direction:",direction)
   c = coord
   # check if first letter is X
   #print("grid letter on coord:", grid[c[0]][c[1]])
   if grid[c[0]][c[1]] == 'X':
      marks.append((c[1],c[0]))
      c = nextc(c,direction)
      if not in_grid(c, grid):
         return []
      # check if second letter is M
      if grid[c[0]][c[1]] == 'M':
         marks.append((c[1],c[0]))
         c = nextc(c,direction)
         if not in_grid(c, grid):
            return [] 
         # check if third letter is A
         if grid[c[0]][c[1]] == 'A':
            marks.append((c[1],c[0]))
            c = nextc(c,direction)
            if not in_grid(c, grid):
               return [] 
            # check if fourth letter is S
            if grid[c[0]][c[1]] == 'S':
               marks.append((c[1],c[0]))
            else:
               marks = []
         else:
             marks = []
      else:
         marks = []
   if len(marks) > 0:
      print("debug: check_path returns:", marks)
   return marks

def traverse(grid):
   occurances = 0
   marked = {}

   dirlist = ['>','<','v','^','d>v','d<v','d>^','d<^']
   for y in range(len(grid)):
      for x in range(len(grid[0])):
         for d in dirlist:
            marks = check_path((y,x),grid,d)
            if len(marks) > 0:
               occurances += 1
            for m in marks:
               marked[m] = '*'

   return (occurances,marked)


# main

# create grid from input
# create copy of grid for marked letters for printing
for line in f:
   print(line.rstrip())
   l = list(line.rstrip())
   grid.append(l)
print_grid(grid,{})

(xmas,marked) = traverse(grid)
print_grid(grid,marked)

print("Number of XMAS found:", xmas)
 
