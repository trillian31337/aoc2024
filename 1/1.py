import re

#f = open('input_test','r')
f = open('input','r')

l1 = []
l2 = []

diff = 0

for line in f:
   l = re.split("\s+", line)
   l1.append(int(l[0]))
   l2.append(int(l[1]))

l1.sort()
l2.sort()
print(l1)
print(l2)
 
for i in range(len(l1)):
   diff += abs(l1[i]-l2[i])
   print("Dist:", abs(l1[i]-l2[i]))

print("Distance between lists:", diff)
 
