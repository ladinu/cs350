#!/usr/bin/env python
from math import floor

def findDoor(wall, door):
   n = len(wall)
   r = int(floor(n/2))
   l = r

   doorFound = False

   count = 0
   while not doorFound and (l >= 0):
      rPos = wall[r]
      lPos = wall[l]

      if rPos == door or lPos == door:
         doorFound = True
         print "Found"

      if r < (n-1):
         r += 1
      l -= 1
      count += 1

findDoor([0, 0, 0, 0, 0, 0, 0], 1)

