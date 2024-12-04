import re

#f = open('input_test','r')
f = open('input','r')

def multiply(p1,p2):
   return p1*p2

data = f.read().rstrip()
mulsum = 0

pattern = re.compile('mul\((\d+),(\d+)\)')
matches = pattern.findall(data)

if matches != None:
   for m in matches:
      print("mul:", m[0], m[1])
      m = multiply(int(m[0]),int(m[1]))
      mulsum += m

print("Added multiplications:", mulsum)

