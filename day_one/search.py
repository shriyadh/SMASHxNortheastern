# Linear Search

import time

def linear_search(array, target):
  
  for num in array:
      if num == target:
          return True
  return False


array = [num for num in range(100000000)] #One hundred million
target = 99999999 # One hundred million - 1

start = time.time()
print(linear_search(array, target))
end = time.time()

print("Time spent: ", end - start)

# Binary Search

import time

def binary_search(array, target):
  low = 0
  high = len(array) - 1
  while low <= high:
      mid = (high + low) // 2
      if array[mid] == target:
          return True
      elif array[mid] < target:
          low = mid + 1
      else:
          high = mid - 1
  return False



array = [num for num in range(100000000)]
target = 99999999

start = time.time()
print(binary_search(array, target))
end = time.time()

print("Time spent:", end - start)
