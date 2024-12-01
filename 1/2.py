import re

#f = open('input_test','r')
f = open('input','r')

l1 = []
l2 = []

sim = 0

for line in f:
   l = re.split("\s+", line)
   l1.append(int(l[0]))
   l2.append(int(l[1]))

for e in l1:
   sim += e * l2.count(e)
   #print("Sim:", e * l2.count(e))

print("Similarity score for lists:", sim)
 
