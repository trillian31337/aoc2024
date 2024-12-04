import re

#f = open('input_test','r')
f = open('input','r')

l = []

safe = 0

def check_diff(a,b,op):
   if op == 'inc':
      return b > a and b - a <= 3
   else:
      return a > b and a - b <= 3


def report_check(report):
   first = report[0]   
   second = report[1]
   if first < second:
      op = 'inc'
   else:
      op = 'dec'
   for i in range(0,len(report)-1):
      if not check_diff(report[i], report[i+1], op):
         return False
   return True

for line in f:
   l.append([int(x) for x in re.split("\s+", line.rstrip())])

for report in l:
   if report_check(report):
      safe += 1
      print(report,end='')
      print('*')
   else:
      print(report)

      
print()

print("Number of safe reports:", safe)
