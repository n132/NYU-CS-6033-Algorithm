# NYU-CS-6033-Algorithm

# Lecture 1

Sort.

Too easy to write something for it.

# Lecture 2

Heap/Priority Queue
[Implementation][./Lec2.py]
- Primitives
  - HEAPIFY: `O(log(n))`
  - PARENT: `O(1)`
  - RIGHT/LEFT: `O(1)`
  - MINUNUM: `O(1)`
  - HEIGHT: `O(1)`
  - EXCHANGE: `O(1)`
- Main Method
  - EXTRACT_MIN: `O(log(n))`
    - Based on HEAPIFY and MINUNUM
  - BUILD_MIN_HEAP: `O(n)`
    - Based on HEAPIFY
  - HEAP_SORT: `O(nlog(n))`
    - Based on BUILD_MIN_HEAP and HEAPIFY
  - DECREASE_KEY: `O(log(n))`
    - Based on HEAPIFY
  - INSERT: `O(log(n))`
    - Based on DECREASE_KEY or HEAPIFY
 
