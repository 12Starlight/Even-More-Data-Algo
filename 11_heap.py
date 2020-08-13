'''
Heap:
  Heaps are one of the slightly more esoteric data structures. The are not asked
  all too often since they often take too much time to build/discuss in a 30 min
  period -- and candidates either know them or not. If you do not know them, you
  are out of luck, which makes these kind of bad questions. But, heaps are often
  used in optimal solutions to 'push' the candidate's knowledge to see how much
  they know.

  Thhe one area heaps are most commonly used is finding the top K elements in 
  some unsorted array. The heap data structure will be able to get you that 
  result without sorting the entire array! The running time for this would be
  O(k * log(n)), whereas a complete sort would require O(n * log(n)) time.

  If you can pont out the heap structure, it would get you more points. A 
  number of languages will have built-in upp[ort for heaps. Like Java has
  'PriorityQueue' and Python has 'heapq'. This is another reason why this 
  question is not great, bc some languages may not have built-in support for
  heaps. So, just know that heaps often are not going to be the 'bulk' of the
  algorithm, though they may be thrown in as a 'follow-up' question sometimes.

'''


# Here is how to use a heap in Python:
import heapq 
nums = [5, 40, 3, 1, 2, 70, 8]

heapq.heapify(nums)
print(nums)

print(heapq.heappop(nums))
print(heapq.heappop(nums))
print(heapq.heappop(nums))
# 3log(n)


arr = [51, 4, 13, 111, 20, 79, 8]

heapq.heapify(arr)
print('')
print(arr)

print(heapq.heappop(arr))
print(heapq.heappop(arr))
print(heapq.heappop(arr))
print(heapq.heappop(arr))
print(heapq.heappop(arr))
print(heapq.heappop(arr))
print(heapq.heappop(arr))


'''

'''