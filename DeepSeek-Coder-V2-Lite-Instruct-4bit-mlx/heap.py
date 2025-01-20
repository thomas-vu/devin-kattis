# Assuming the template has been provided as heap.cpp and heap.h
# Here is the implementation of a binary max-heap in C++ based on the given template:

# heap.h
#ifndef HEAP_H
#define HEAP_H

#include <vector>
#include <stdexcept>

class MaxHeap {
private:
    std::vector<int> heap;

    int parent(int i) { return (i - 1) / 2; }
    int leftChild(int i) { return 2 * i + 1; }
    int rightChild(int i) { return 2 * i + 2; }

    void heapifyUp(int index);
    void heapifyDown(int index);

public:
    MaxHeap() {}
    void insert(int value);
    int remove();
    int size();
    int maximum();
};

#endif // HEAP_H

# heap.cpp
#include "heap.h"

void MaxHeap::heapifyUp(int index) {
    while (index > 0 && heap[parent(index)] < heap[index]) {
        std::swap(heap[parent(index)], heap[index]);
        index = parent(index);
    }
}

void MaxHeap::heapifyDown(int index) {
    int largest = index;
    int left = leftChild(index);
    int right = rightChild(index);

    if (left < heap.size() && heap[left] > heap[largest]) {
        largest = left;
    }
    if (right < heap.size() && heap[right] > heap[largest]) {
        largest = right;
    }
    if (largest != index) {
        std::swap(heap[index], heap[largest]);
        heapifyDown(largest);
    }
}

void MaxHeap::insert(int value) {
    heap.push_back(value);
    heapifyUp(heap.size() - 1);
}

int MaxHeap::remove() {
    if (heap.empty()) {
        throw std::out_of_range("Heap is empty");
    }
    int root = heap[0];
    heap[0] = heap.back();
    heap.pop_back();
    if (!heap.empty()) {
        heapifyDown(0);
    }
    return root;
}

int MaxHeap::size() {
    return heap.size();
}

int MaxHeap::maximum() {
    if (heap.empty()) {
        throw std::out_of_range("Heap is empty");
    }
    return heap[0];
}