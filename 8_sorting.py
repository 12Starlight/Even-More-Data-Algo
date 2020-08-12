'''
Sorting
  O(N * Log(N)) Time

  Think about whether the solution needs to be partially sorted bc sometimes it
  is best to not use divide and conqure types of sort.

'''


arr = [1, 2, 8, 9, 5, 3, 4, 7, 6]


# iterates through array swapping elements to find the smallest
def bubbleSort(arr):
  n = len(arr)
  for i in range(n):
    for j in range(0, n - i - 1):
      if arr[j] > arr[j + 1]:
        arr[j], arr[j + 1] = arr[j + 1], arr[j]

bubbleSort(arr)
print(arr)
print('')

# inserts every array element into its proper position by shifting the number
def insertionSort(arr):
  for i in range(1, len(arr)):
    key = arr[i]
    j = i - 1
    while j >= 0 and key < arr[j]:
      arr[j + 1] = arr[j]
      j -= 1
    arr[j + 1] = key

insertionSort(arr)
print(arr)
print('')

# iterates through array finding smallest element to insert
def selectionSort(arr):
  for i in range(len(arr)):
    min_idx = i
    for j in range(i + 1, len(arr)):
      if arr[min_idx]  > arr[j]:
        min_idx = j
    arr[i], arr[min_idx] = arr[min_idx], arr[i]

selectionSort(arr)
print(arr)
print('')