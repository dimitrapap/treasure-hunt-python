# -*- coding: utf-8 -*-
import math
import random
#the variables a and b correspond to the players position
#the variables c and d correspond to the treasures position
a=random.randint(0,9)
b=random.randint(0,9)
c=random.randint(0,9)
d=random.randint(0,9)

while a!=c and b!=d :
  direction=raw_input("give direction (e.g right, left, up, down)")
  if (direction == "right"):
   b=b+1
  elif (direction == "left"):
   b=b-1
  elif (direction == "up"):
   a=a-1
  elif (direction == "down"):
   a=a+1
  e=math.fabs(a-c)
  f=math.fabs(b-d)
  g=e*f
  print "you need", g , "more squares to find the treasure"

print "Congratulations you found the treasure!"
