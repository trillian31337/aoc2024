import re

#f = open('input_test','r')
f = open('input','r')

def multiply(p1,p2):
   return p1*p2

def find_mul(dataslice):
   mpattern = re.compile('mul\((\d+),(\d+)\)')
   matches = mpattern.findall(dataslice)
   msum = 0
   if matches != None:
      for m in matches:
         print("mul:", m[0], m[1])
         m = multiply(int(m[0]),int(m[1]))
         msum += m
   return msum

data = f.read().rstrip()
mulsum = 0

dopattern = re.compile("do\(\)")
dontpattern = re.compile("don\'t\(\)")

toggle = 'do'
index = 0

while index < len(data):
   # find next don't() operation after current index
   m = dontpattern.search(data, index) 
   # run find_mul() on slice from index to start of don't operation
   if m != None:
      print("Start of next don't operation:", m.start())
      mulsum += find_mul(data[index:m.start()])
   else:
      # no more don't operation, parse the rest of the string
      mulsum += find_mul(data[index:])
      break
   # find next do() operation
   index = m.end()
   m = dopattern.search(data,index)
   # change index
   if m!= None:
      print("Start of next do operation:", m.start())
      index = m.end()
   else:
      # no more do operation, finished
      break

print("Added multiplications:", mulsum)

