#!/usr/bin/env python

LEFT = 'left'
RIGHT = 'right'

class Element:
   def __init__(self, value, direction):
      self.value = value;
      self.direction = direction

   def __repr__(self):
      direction = ''
      if self.direction == LEFT:
         direction = "<-"
      else:
         direction = "->"
      return "{%i %s}" % (self.value, direction)

   def reverseDirection(self):
      if self.direction == LEFT:
         self.direction = RIGHT
      else:
         self.direction = LEFT

class Permutation:
   def __init__(self):
      self.array = []
      self.length = 0

   def __repr__(self):
      ret = "[ "
      for i in self.array:
         ret += str(i)
         ret += " "
      return ret + "]"

   def push(self, element):
      self.array.append(element)
      self.length += 1
      assert self.length == len(self.array)

   def get(self, index):
      return self.array[index]


   def pushTo(self, targetArray):
      elements = ''
      for i in self.array:
         elements += str(i.value)
      targetArray.append(elements)

   def toInt(self):
      elements = ''
      for i in self.array:
         elements += str(i.value)
      return int(elements)

   # Check if elemnt at given index is mobile by seeing if the
   # element that its pointing to is smaller. Will return a boolean
   def isMobile(self, index):
      element = self.array[index]
      adjElement_index = index

      if element.direction == LEFT:
         adjElement_index = index - 1
      else:
         adjElement_index = index + 1

      # If the arrow point off index, by definition
      # the element is not mobile
      if (adjElement_index < 0) or (adjElement_index >= self.length):
         return False

      adjElement = self.array[adjElement_index]

      # Current element is only mobile if its bigger than the 
      # elemnt that it is pointing to
      return element.value > adjElement.value

   def hasMobileElement(self):
      for index, element in enumerate(self.array):
         if self.isMobile(index):
            return True
      return False

   # Does a linear search through the internal array to find
   # the largest mobile element. If such element was found
   # the index will be returned, else -1 will be reutned
   def largestMobile(self):
      if self.length < 2:
         return -1

      largestElement = Element(-1, LEFT)
      largestElementIndex = -1

      for index, element in enumerate(self.array):
         if self.isMobile(index):
            if element.value > largestElement.value:
               largestElement = element
               largestElementIndex = index

      return largestElementIndex

   def swap(self, i, j):
      arr = self.array
      arr[i], arr[j] = arr[j], arr[i]

   def reverseElements(self, k):
      element = self.array[k]
      for i in self.array:
         if i.value > element.value:
            i.reverseDirection()


# Convert a given number to a list of elements
# Each element has a value and a direction where
# the arrow point to. Initially, they will all
# point to the left 
def init_perm(n):
   permutation = Permutation()
   i = 0
   while i < n:
      permutation.push(Element(i+1, LEFT))
      i += 1

   return permutation


def johnsonTrotterPrint(n):
   lastPermutaion = init_perm(n)
   print lastPermutaion.toInt()

   while lastPermutaion.hasMobileElement():
      lastPermutaion = johnsonTrotterCore(lastPermutaion)
      if not lastPermutaion:
         break
      print lastPermutaion.toInt()

def johnsonTrotter(n):
   permutationList = []
   lastPermutaion = init_perm(n)
   lastPermutaion.pushTo(permutationList)

   while lastPermutaion.hasMobileElement():
      lastPermutaion = johnsonTrotterCore(lastPermutaion)
      if not lastPermutaion:
         break
      lastPermutaion.pushTo(permutationList)

   return permutationList

def johnsonTrotterCore(permutation):
      # Find index of largest mobile element
      k = permutation.largestMobile()
      if k < 0:
         return False
      # Swap largest mobile with its adjacent 
      # element pointed by the arrow
      element = permutation.get(k)
      adjElement_index = k

      if element.direction == LEFT:
         adjElement_index = k - 1
      else:
         adjElement_index = k + 1

      permutation.swap(k, adjElement_index)
      # We just swapped this, so index must change
      k = adjElement_index

      # Reverse the direction of all alements that are
      # larger than k
      permutation.reverseElements(k)
      return permutation
