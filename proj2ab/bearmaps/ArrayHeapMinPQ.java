package bearmaps;

import java.util.HashMap;
import java.util.NoSuchElementException;

public class ArrayHeapMinPQ<T> implements ExtrinsicMinPQ<T> {
    private class Node {
        private T theItem;
        private double myPriority;

        private Node(T item, double priority) {
            theItem = item;
            myPriority = priority;
        }

        public T item(){
            return theItem;
        }

        public double priority() {
            return myPriority;
        }

        @Override
        public String toString() {
            return theItem.toString() + ", " + myPriority;
        }
    }

    /**
     * Throws an exception if the index is invalid for sinking or swimming.
     */
    private void validateSinkSwimIndex(int index) {
        if (index < 1) {
            throw new IllegalArgumentException("Cannot sink or swim nodes with index 0 or less");
        }
        if (index > size) {
            throw new IllegalArgumentException("Cannot sink or swim nodes with index greater than current size.");
        }
        if (heap[index] == null) {
            throw new IllegalArgumentException("Cannot sink or swim a null node.");
        }
    }

    private Node[] heap;
    private int size;
    private HashMap<T, Double> allItem;

    public ArrayHeapMinPQ() {
        heap = new ArrayHeapMinPQ.Node[16];
        size = 0;
        heap[0] = null;
        allItem = new HashMap();
    }

    /**
     * Returns the index of the node to the left of the node at i.
     */
    private static int leftIndex(int i) {
        return 2 * i;
    }

    /**
     * Returns the index of the node to the right of the node at i.
     */
    private static int rightIndex(int i) {
        return 2 * i + 1;
    }

    /**
     * Returns the index of the node that is the parent of the node at i.
     */
    private static int parentIndex(int i) {
        return i / 2;
    }

    /**
     * Gets the node at the ith index, or returns null if the index is out of
     * bounds.
     */
    private Node getNode(int index) {
        if (!inBounds(index)) {
            return null;
        }
        return heap[index];
    }

    /**
     * Returns true if the index corresponds to a valid item. For example, if
     * we have 5 items, then the valid indices are 1, 2, 3, 4, 5. Index 0 is
     * invalid because we leave the 0th entry blank.
     */
    private boolean inBounds(int index) {
        if ((index > size) || (index < 1)) {
            return false;
        }
        return true;
    }

    /**
     * Swap the nodes at the two indices.
     */
    private void swap(int index1, int index2) {
        Node node1 = getNode(index1);
        Node node2 = getNode(index2);
        heap[index1] = node2;
        heap[index2] = node1;
    }


    /**
     * Returns the index of the node with smaller priority.
     * Not both nodes are null.
     */
    private int min(int index1, int index2) {
        Node node1 = getNode(index1);
        Node node2 = getNode(index2);
        if (node1 == null) {
            return index2;
        } else if (node2 == null) {
            return index1;
        } else if (node1.myPriority < node2.myPriority) {
            return index1;
        } else {
            return index2;
        }
    }

    /**
     * Bubbles up the node currently at the given index.
     */
    private void swim(int index) {
        // Throws an exception if the given index is invalid.
        validateSinkSwimIndex(index);

        if (index == 1)  {
            return;
        } else if (min(index, parentIndex(index)) == parentIndex(index)) {
            return;
        } else {
            swap(index, parentIndex(index));
            swim(parentIndex(index));
        }
    }

    /**
     * Bubbles down the node currently at the given index.
     */
    private void sink(int index) {
        // Throws an exception if the given index is invalid.
        validateSinkSwimIndex(index);

        if (index == size || index * 2 > size || index * 2 + 1 > size)  {
            return;
        }
        if (min(index, 2 * index) != index)  {
            swap(index, 2 * index);
            sink(2 * index);
        }
        if (min(index, 2 * index + 1) != index) {
            swap(index, 2 * index + 1);
            sink(2 * index + 1);
        }
    }

    /** Helper function to resize the backing array when necessary. */
    private void resize(int capacity) {
        Node[] temp = new ArrayHeapMinPQ.Node[capacity];
        for (int i = 1; i < this.heap.length; i++) {
            temp[i] = this.heap[i];
        }
        this.heap = temp;
    }

    /* Adds an item with the given priority value. Throws an
     * IllegalArgumentException if item is already present. */
    public void add(T item, double priority) {
        if (contains(item)) {
            throw new IllegalArgumentException();
        }

        if (size + 1 == heap.length) {
            resize(heap.length *2);
        }
        heap[size + 1] = new Node(item, priority);
        size ++;
        swim(size);
        allItem.put(item, priority);
    }
    /* Returns true if the PQ contains the given item. */
    public boolean contains(T item) {
        return allItem.containsKey(item);
    }
    /* Returns the minimum item. Throws NoSuchElementException if the PQ is empty. */
    public T getSmallest() {
        return heap[1].item();
    }
    /* Removes and returns the minimum item. Throws NoSuchElementException if the PQ is empty. */
    public T removeSmallest() {
        T smallest = heap[1].item();
        heap[1] = heap[size];
        heap[size] = null;
        sink(1);
        size -= 1;
        allItem.remove(smallest);
        return smallest;
    }
    /* Returns the number of items in the PQ. */
    public int size() {
        return size;
    }
    /* Changes the priority of the given item. Throws NoSuchElementException if the item
     * doesn't exist. */
    public void changePriority(T item, double priority) {
        if (!contains(item)) {
            throw new NoSuchElementException();
        }
        double oldPriority = allItem.get(item);
        changePriorityHelper(item, oldPriority, priority, 1);
    }

    private void changePriorityHelper(T item, double oldPriority, double newPriority, int index) {
        if (heap[index].item().equals(item)) {
            heap[index] = new Node(item, newPriority);
            sink(index);
            swim(index);
        }
        if (oldPriority > heap[index].priority()) {
            changePriorityHelper(item, oldPriority, newPriority, leftIndex(index));
            changePriorityHelper(item, oldPriority, newPriority, rightIndex(index));
        }
    }
}
