# DSA_HYBRID_PRIORITYQUEUE

Implemented a hybrid priority-queue using heap and hash-maps to improve the search time complexity.

## Introduction

This repository contains the implementation of a hybrid priority queue, which combines a min-heap and a hash map to efficiently handle prioritized elements. The hybrid data structure offers fast insertion, deletion, and retrieval operations based on both priority and name.

## Implementation Details

The implementation of the hybrid priority queue is done using the combining min-heap and hash-map approach. The `HybridPriorityQueue` class is defined with two main attributes: `heap` and `map`. The `heap` stores the element details, while the `map` is used as a hash map to map priorities to their corresponding indices in the heap.

## Features

- **Insertion and Deletion**: On average, both insertion and deletion can be performed in O(log n) time.
- **Search by Identifier**: Average time complexity is O(1).
- **Retrieve Highest Priority Element**: Can be retrieved in O(1) average time.
- **Space Efficiency**: Uses O(n) memory space.


## Practical Applications

The hybrid priority queue has practical applications in scenarios where elements need to be prioritized based on their priorities and retrieved or updated efficiently using their names. Some examples include task scheduling, job prioritization, event handling, resource allocation, hospital management, and online ticketing systems.

## Contributions

Contributions to this project are welcome. If you find any issues or have suggestions for improvements, please feel free to open an issue or submit a pull request.
