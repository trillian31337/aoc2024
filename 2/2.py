import re
from termcolor import colored

f = open('input_test','r')
#f = open('input','r')

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

def report_check_dampener(report):
   if report_check(report):
      return True,-1
   for i in range(len(report)):
      r = report.copy()
      r.pop(i)
      if report_check(r):
         return True,i
   return False,-1   

def print_report(report,res,index):
   if res == False:
      color = 'dark_grey'
   else:
      color = 'white'
   for i in range(len(report)):
      if index == i:
         print(colored(report[i],'red'),end=' ')
      else:
         print(colored(report[i],color),end=' ')
   print()
 

for line in f:
   l.append([int(x) for x in re.split("\s+", line.rstrip())])

for report in l:
   res,index = report_check_dampener(report)
   if res == True:
      safe += 1
   print_report(report,res,index)
      
print()

print("Number of safe reports:", safe)
