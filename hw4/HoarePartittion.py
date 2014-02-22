
def hp(A, l, r):
   p = A[l]
   i = l
   j = r

   while i < j:
      while A[i] < p:
         i = i + 1
      while A[j] > p:
         j = j - 1
      swap(A, i, j)

   swap(A, i, j)
   swap(A, l, j)
   return j
def partition(myList, start, end):
    pivot = myList[start]
    left = start+1
    right = end
    done = False
    while not done:
        while left <= right and myList[left] <= pivot:
            left = left + 1
        while myList[right] >= pivot and right >=left:
            right = right -1
        if right < left:
            done= True
        else:
            # swap places
            temp=myList[left]
            myList[left]=myList[right]
            myList[right]=temp
    # swap start with myList[right]
    temp=myList[start]
    myList[start]=myList[right]
    myList[right]=temp
    return right


def printDent(start, end, pivot, level):
   a = "-"
   s = "i=%s, r=%s  : s=%s" % (start, end, pivot)
   for i in range(level):
      a = a + a
   #print a + s

def qs(myList, start, end, indent):
   pivot = None
   if start < end:
      # partition the list
      pivot = partition(myList, start, end)
      # sort both halves
      qs(myList, start, pivot-1, indent + 1)
      qs(myList, pivot+1, end, indent + 1)
   printDent(start, end, pivot, indent)
   print myList
   return myList

print qs([5, 3, 1, 9, 8, 2, 4, 7], 0, 7, 0)

print
print

print qs(['A', 'L', 'G', 'O', 'R', 'I', 'T', 'H', 'M'], 0, 8, 0)

