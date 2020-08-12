'''
Sorting
  O(N * Log(N)) Time

  Think about whether the solution needs to be partially sorted bc sometimes it
  is best to not use divide and conqure types of sort.

'''


# iterates through array swapping elements to find the smallest
def bubbleSort(arr):
  n = len(arr)
  for i in range(n):
    for j in range(0, n - i - 1):
      if arr[j] > arr[j + 1]:
        arr[j], arr[j + 1] = arr[j + 1], arr[j]

# inserts every array element into its proper position by shifting the number
def insertionSort(arr):
  for i in range(1, len(arr)):
    key = arr[i]
    j = i - 1
    while j >= 0 an key < arr[j]:
      arr[j + 1] = arr[j]
      j--
    arr[j + 1] = key