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

def check_X(coord,grid):
   marks = []  
   # middle of X-MAS is the letter A, already checked
   
   # fetch coordinates for first diagonal
   c1 = nextc(coord,'d<^')
   c2 = nextc(coord,'d>v')
   if not in_grid(c1,grid) or not in_grid(c2,grid):
       return []

   # fetch coordinates for second diagonal
   c3 = nextc(coord,'d>^')
   c4 = nextc(coord,'d<v')
   if not in_grid(c3,grid) or not in_grid(c4,grid):
       return []

   # fetch letters and check
   l1 = grid[c1[0]][c1[1]]
   l2 = grid[c2[0]][c2[1]]
   l3 = grid[c3[0]][c3[1]]
   l4 = grid[c4[0]][c4[1]]
   if ('M' in [l1,l2] and 'S' in [l1,l2]) and ('M' in [l3,l4] and 'S' in [l3,l4]):
       # found an X
       marks.append((coord[1],coord[0]))
       marks.append((c1[1],c1[0]))
       marks.append((c2[1],c2[0]))
       marks.append((c3[1],c3[0]))
       marks.append((c4[1],c4[0]))
       return marks

   # no X
   return []


def check_path(coord,grid,direction):
   marks = []

   c = coord
   # check if first letter is X
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
   return marks

def traverse(grid):
   occurances = 0
   marked = {}

   for y in range(len(grid)):
      for x in range(len(grid[0])):
         if grid[y][x] == 'A':
            marks = check_X((y,x),grid)
            if len(marks) > 0:
               occurances += 1
            for m in marks:
               marked[m] = '*'

   return (occurances,marked)


# main

# create grid from input
# create copy of grid for marked letters for printing
for line in f:
   l = list(line.rstrip())
   grid.append(l)

(xmas,marked) = traverse(grid)
print_grid(grid,marked)

print("Number of XMAS found:", xmas)
 
