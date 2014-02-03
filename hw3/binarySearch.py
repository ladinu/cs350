#!/usr/bin/env python
from math import floor


def bs(arr, key):
   compCount = 0
   n = len(arr)
   l = 0
   r = n-1
   while l <= r:
      m = int(floor((l+r)/2.0))
      compCount += 1
      if key == arr[m]:
         return (m, compCount)
      elif key < arr[m]:
         r = m - 1
      else:
         l = m + 1

   return (-1, compCount)

a = [5, 13, 19, 23, 28, 30, 49, 57, 89, 92, 94, 97]

compList = []

for i in a:
   print "searched for " + str(i) + " got comparisons " + str(bs(a, i)[1]) 

print
print "searched for " + str(58) + " got comparisons " + str(bs(a, 58)[1]) 

