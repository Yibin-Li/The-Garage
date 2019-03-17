package bearmaps;
import java.util.HashMap;
import java.util.NoSuchElementException;

//import static org.junit.Assert.assertEquals;

// import static org.junit.Assert.assertEquals;


public class ArrayHeapMinPQ<T> implements ExtrinsicMinPQ<T> {
    private PriorityNode[] priorityQueue;
    private int size;
    private HashMap<T, Integer> hash;

    public ArrayHeapMinPQ() {
        priorityQueue = new ArrayHeapMinPQ.PriorityNode[16];
        size = 0;
        priorityQueue[0] = null;
        hash = new HashMap();
    }

    private int parent(int index) {
        int temp;
        temp = index / 2;
        return temp;
    }

    private int leftChild(int index) {
        return index * 2;
    }

    private int rightChild(int index) {
        return index * 2 + 1;
    }

//    private void validAnnounce(int index) {
//        if (index < 1) {
//            throw new IllegalArgumentException("index < 1");
//        }
//        if (index > size) {
//            throw new IllegalArgumentException("index > size");
//        }
//        if (priorityQueue[index] == null) {
//            throw new IllegalArgumentException("priorityQueue[index] == null");
//        }
//    }

    private boolean valid(int index) {
        if ((index < 1) || (index > size)) {
            return false;
        }
        return true;
    }


    private void swap(int index1, int index2) {
        PriorityNode node1 = getNode(index1);
        PriorityNode node2 = getNode(index2);
        priorityQueue[index1] = node2;
        priorityQueue[index2] = node1;
        // hash, index does not change, but put items to different index
        hash.put(node1.item, index2);
        hash.put(node2.item, index1);
    }

    private PriorityNode getNode(int index) {
        if (!valid(index)) {
            return null;
        }
        return priorityQueue[index];
    }

    public int getIndex(T item) {
        // how to go through hashmap, using item to find index
        return hash.get(item);
    }

    private void swim(int index) {
        // if reach root, stop
        // if reach parent.priority < self.priority, stop

//        validAnnounce(index);
        if (size == 0) {
            return;
        }

        if (index == 1)  {
            return;
        } else if (min(index, parent(index)) == parent(index)) {
            return;
        } else {
            swap(index, parent(index));
            swim(parent(index));
        }
        // what is stop
    }

    private void sink(int index) {
        // min can take in one null, but cannot take in two null
        // thus, have to check both null
        
        if (!valid(rightChild(index)) && (!valid(leftChild(index)))) {
            return;
        }
        int smaller = min(leftChild(index), rightChild(index));
        if (min(smaller, index) != index) {
            swap(smaller, index);
            sink(smaller);
        }
    }


    private int min(int index1, int index2) {
        PriorityNode node1 = getNode(index1);
        PriorityNode node2 = getNode(index2);
        if (node1 == null) {
            return index2;
        } else if (node2 == null) {
            return index1;
        } else if (node1.priority < node2.priority) {
            return index1;
        } else {
            return index2;
        }
    } // return an index whose priorityNode's priority is higher

    private void resize(int capacity) {
        PriorityNode[] temp = new ArrayHeapMinPQ.PriorityNode[capacity];
        for (int i = 1; i < this.priorityQueue.length; i++) {
            temp[i] = this.priorityQueue[i];
        }
        this.priorityQueue = temp;
    }


    public boolean contains(T item) {
        return hash.containsKey(item);
    } // Returns true if the PQ contains the given item.

    public void add(T item, double priority) {
        if (contains(item)) {
            throw new IllegalArgumentException();
        }
        if (size + 1 == priorityQueue.length) {
            resize(priorityQueue.length * 2);
        }
        priorityQueue[size + 1] = new PriorityNode(item, priority);
        size++;
        swim(size);
        hash.put(item, size);
    } // Adds an item of type T with the given priority.
    // If the item already exists, throw an IllegalArgumentException.
    // You may assume that item is never null.
    // there cannot be two same items
    // remember to resize array

    public T getSmallest() {
        if (size == 0) {
            throw new NoSuchElementException();
        }
        return priorityQueue[1].item;
    } // Returns the item with smallest priority. If no items exist, throw a NoSuchElementException.

    public T removeSmallest() {
        // return the min
        // swap the item at root with the item of the right-most leaf node
        // remove the right-most leaf node
        // sink the root node
        if (size == 0) {
            throw new NoSuchElementException();
        }
        T smallest = priorityQueue[1].item;
        swap(1, size);
        sink(1);
//        priorityQueue[size] = null;
        size -= 1;
        // exception index > size
        // when size = 0, still call
        hash.remove(smallest);
        return smallest;
    } // Removes and returns the item with smallest priority.
    // If no items exist, throw a NoSuchElementException.
    // If using an array representation for your min heap,
    // it should never be more than approximately 3/4s empty.

    public int size() {
        return size;
    } // Returns the number of items.

    public void changePriority(T item, double priority) {
        // how to find that item, find the priority node of the item
        // find the item(find its prioritynode)
        // change its priority
        // sink or swim, how to judge whether sink or swim, if priority > origin priority, sink
        if (!contains(item)) {
            throw new NoSuchElementException();
        }
        // use hash to find index using item
        // use that index to access priorityQueue, get that prioritynode, get that index
        int i = getIndex(item);
        PriorityNode temp = priorityQueue[i];
        temp.priority = priority;
        priorityQueue[i] = temp;
        sink(i);
        swim(i);
    } // Sets the priority of the given item to the given value.
    // If the item does not exist, throw a NoSuchElementException.

    // There may only be one copy of a given item in the priority queue at any time.
    // if you try to add an item that is equal to
    // another according to .equals, the PQ should throw an exception.

    // If there are 2 items with the same priority, you may break ties arbitrarily.

    private class PriorityNode {
        private T item;
        private double priority;

        PriorityNode(T e, double p) {
            this.item = e;
            this.priority = p;
        }

    }

//    public static void main(String[] args) {
//
//        // without swapping, getIndex should be correct, because it is based on hash
//        ArrayHeapMinPQ<String> pq1 = new ArrayHeapMinPQ<>();
//        pq1.add("a", 1);
//        pq1.add("b", 2);
//        pq1.add("c", 3);
//        pq1.add("d", 4);
//        pq1.add("e", 5);
//        int actual1 = pq1.getIndex("c");
//        assertEquals(3, actual1);
//
//        // test getIndex, with hash
//        ArrayHeapMinPQ<String> pq = new ArrayHeapMinPQ<>();
//        pq.add("c", 3);
//        pq.add("i", 9);
//        pq.add("g", 7);
//        pq.add("d", 4);
//        pq.add("a", 1);
//
//        int actual = pq.getIndex("c");
//        assertEquals(2, actual);
//
//        // test change priority simple
//        ArrayHeapMinPQ<String> pq2 = new ArrayHeapMinPQ<>();
//        pq2.add("a", 1);
//        pq2.add("b", 2);
//        pq2.add("c", 3);
//        pq2.add("d", 4);
//        pq2.add("e", 5);
//        int actual2 = pq2.getIndex("e");
//        assertEquals(true, pq2.contains("e"));
//        assertEquals(5, actual2);
//        pq2.changePriority("e", 1);
//        int actual3 = pq2.getIndex("e");
//        assertEquals(2, actual3);
//
//        // test change priority complex
//        ArrayHeapMinPQ<String> pq3 = new ArrayHeapMinPQ<>();
//        pq3.add("c", 3);
//        pq3.add("i", 9);
//        pq3.add("g", 7);
//        pq3.add("d", 4);
//        pq3.add("a", 1);
//        pq3.add("h", 8);
//        pq3.add("e", 5);
//        pq3.add("b", 2);
//        pq3.add("j", 3);
//        pq3.add("k", 4);
//        pq3.changePriority("i", 1);
//        assertEquals(2, pq3.getIndex("i"));

//    }
}

