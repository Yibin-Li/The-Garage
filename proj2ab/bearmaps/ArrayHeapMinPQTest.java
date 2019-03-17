package bearmaps;

import edu.princeton.cs.algs4.Stopwatch;
import org.junit.Test;

import static org.junit.Assert.*;
import static org.junit.Assert.assertTrue;


public class ArrayHeapMinPQTest {
    // passed size, contains, getsmallest, changepriority
    // random int -> if 1 , add

//    public void randomizeMethod(ArrayHeapMinPQ ah, int id, int i) {
//        if (id == 1) {
//            ah.add("hello" + i, i);
//        } else if (id == 2) {
//            ah.size();
//        } else if (id == 3) {
//            ah.changePriority("helloOrigin", 999999999);
//        } else if (id == 4) {
//            ah.removeSmallest();
//        } else if (id == 5) {
//            ah.getSmallest();
//        } else if (id == 6) {
//            ah.contains("helloOrigin");
//        }
//    }

//    @Test
//    public void testRandom() {
//        ArrayHeapMinPQ<String> ah1 = new ArrayHeapMinPQ<>();
//        ah1.add("helloOrigin", 99999999);
//
//
//        for(int i = 0; i < 40000; i++) {
//            int rand = (int)(Math.random() * 6) + 1;
//            randomizeMethod(ah1, rand, i);
//        }
//
//    }


    @Test
    public void testTimeChangePriority() {
        ArrayHeapMinPQ<String> ah1 = new ArrayHeapMinPQ<>();
        for(int i = 0; i < 40000; i++) {
            ah1.add("hello" + i, i + 1);
            ah1.add("hi" + i, i + 1);
        }

        Stopwatch sw1 = new Stopwatch();
        for(int i = 0; i < 40000; i++){
            ah1.changePriority("hello" + i, 40000 - i);
        }

        System.out.println("Total time elapsed for 4000_ArrayHeapMinPQ: "
                + sw1.elapsedTime() + " seconds.");

        NaiveMinPQ<String> na1 = new NaiveMinPQ<>();
        for(int i = 0; i < 40000; i++) {
            na1.add("hello" + i, i + 1);
            na1.add("hi" + i, i + 1);
        }

        Stopwatch sw2 = new Stopwatch();
        for(int i = 0; i < 40000; i++){
            na1.changePriority("hello" + i, 40000 - i);
        }

        System.out.println("Total time elapsed for 4000_NaiveHeapMinPQ: "
                + sw2.elapsedTime() + " seconds.");
    }

    @Test
    public void testTimeRemoveSmallest() {
        ArrayHeapMinPQ<String> ah1 = new ArrayHeapMinPQ<>();
        for(int i = 0; i < 40000; i++) {
            ah1.add("hello" + i, i + 1);
            ah1.add("hi" + i, i + 1);
        }

        Stopwatch sw1 = new Stopwatch();
        for(int i = 0; i < 40000; i++){
            ah1.removeSmallest();
        }

        System.out.println("Total time elapsed for 1000_ArrayHeapMinPQ: "
                + sw1.elapsedTime() + " seconds.");

        NaiveMinPQ<String> na1 = new NaiveMinPQ<>();
        for(int i = 0; i < 40000; i++) {
            na1.add("hello" + i, i + 1);
            na1.add("hi" + i, i + 1);
        }

        Stopwatch sw2 = new Stopwatch();
        for(int i = 0; i < 40000; i++){
            na1.removeSmallest();
        }

        System.out.println("Total time elapsed for 1000_NaiveHeapMinPQ: "
                + sw2.elapsedTime() + " seconds.");
    }

    @Test
    public void testTimeSize() {
        ArrayHeapMinPQ<String> ah1 = new ArrayHeapMinPQ<>();
        for(int i = 0; i < 1000000; i++) {
            ah1.add("hello" + i, i + 1);
            ah1.add("hi" + i, i + 1);
        }

        Stopwatch sw1 = new Stopwatch();
        for(int i = 0; i < 1000000; i++){
            ah1.size();
        }

        System.out.println("Total time elapsed for 4000_ArrayHeapMinPQ: "
                + sw1.elapsedTime() + " seconds.");

        NaiveMinPQ<String> na1 = new NaiveMinPQ<>();
        for(int i = 0; i < 1000000; i++) {
            na1.add("hello" + i, i + 1);
            na1.add("hi" + i, i + 1);
        }

        Stopwatch sw2 = new Stopwatch();
        for(int i = 0; i < 1000000; i++){
            ah1.size();
        }

        System.out.println("Total time elapsed for 4000_NaiveHeapMinPQ: "
                + sw2.elapsedTime() + " seconds.");
    }


    @Test
    public void testTime2(){
        ArrayHeapMinPQ<String> ah1 = new ArrayHeapMinPQ<>();
        for(int i = 0; i < 1000; i++) {
            ah1.add("hello" + i, i + 1);
            ah1.add("hi" + i, i + 1);
        }

        Stopwatch sw1 = new Stopwatch();
        for(int i = 0; i < 1000; i++){

            ah1.getSmallest();
            ah1.changePriority("hello" + i, 1000 - i);
            ah1.contains("hello" + i);
            ah1.size();
            ah1.removeSmallest();
        }

        System.out.println("Total time elapsed for 1000_ArrayHeapMinPQ: "
                + sw1.elapsedTime() + " seconds.");

        ArrayHeapMinPQ<String> ah2 = new ArrayHeapMinPQ<>();
        Stopwatch sw2 = new Stopwatch();

        for(int i = 0; i < 10000; i++){
            ah2.add("hello" + i, i+1);
            ah2.add("hi" + i, i+1);
            ah2.getSmallest();
            ah2.changePriority("hello" + i, 10000 - i);
            ah2.contains("hello" + i);
            ah2.size();
            ah2.removeSmallest();
        }
        System.out.println("Total time elapsed for 10000_ArrayHeapMinPQ: "
                + sw2.elapsedTime() + " seconds.");

        ArrayHeapMinPQ<String> ah3 = new ArrayHeapMinPQ<>();
        for(int i = 0; i < 40000; i++){
            ah3.add("hello" + i, i+1);
            ah3.add("hi" + i, i+1);
        }

        Stopwatch sw3 = new Stopwatch();

        for(int i = 0; i < 40000; i++){
            ah3.getSmallest();
            ah3.changePriority("hello" + i, 40000 - i);
            ah3.contains("hello" + i);
            ah3.size();
            ah3.removeSmallest();
        }
        System.out.println("Total time elapsed for 40000-_ArrayHeapMinPQ: "
                + sw3.elapsedTime() + " seconds.");

    }

    @Test
    public void testTime3(){

        Stopwatch sw1 = new Stopwatch();
        NaiveMinPQ<String> na1 = new NaiveMinPQ<>();
        for(int i = 0; i < 1000; i++){
            na1.add("hello" + i, i+1);
            na1.add("hi" + i, i+1);
            na1.getSmallest();
            na1.changePriority("hello" + i, 1000 - i);
            na1.contains("hello" + i);
            na1.size();
            na1.removeSmallest();
        }
        System.out.println("Total time elapsed for 1000_NaiveMinPQ: "
                + sw1.elapsedTime() + " seconds.");

        Stopwatch sw2 = new Stopwatch();
        NaiveMinPQ<String> na2 = new NaiveMinPQ<>();
        for(int i = 0; i < 10000; i++){
            na2.add("hello" + i, i+1);
            na2.add("hi" + i, i+1);
            na2.getSmallest();
            na2.changePriority("hello" + i, 10000 - i);
            na2.contains("hello" + i);
            na2.size();
            na2.removeSmallest();
        }
        System.out.println("Total time elapsed for 10000_NaiveMinPQ: "
                + sw2.elapsedTime() + " seconds.");

        Stopwatch sw3 = new Stopwatch();
        NaiveMinPQ<String> na3 = new NaiveMinPQ<>();
        for(int i = 0; i < 40000; i++){
            na3.add("hello" + i, i+1);
            na3.add("hi" + i, i+1);
            na3.getSmallest();
            na3.changePriority("hello" + i, 40000 - i);
            na3.contains("hello" + i);
            na3.size();
            na3.removeSmallest();
        }
        System.out.println("Total time elapsed for 40000_NaiveMinPQ: "
                + sw3.elapsedTime() + " seconds.");

    }


    @Test
    public void testAdd1SizeContains() {
        ArrayHeapMinPQ<String> ah = new ArrayHeapMinPQ<>();
        ah.add("a", 1);
        ah.add("d", 4);
        ah.add("c", 3);
        ah.add("b", 2);
        ah.add("e", 5);
        assertEquals(ah.getSmallest(), "a");
        assertTrue(ah.contains("a"));
        assertEquals(ah.size(), 5);
        assertEquals(ah.removeSmallest(), "a");
        assertFalse(ah.contains("a"));
        assertEquals(ah.size(), 4);
        //System.out.println(ah.getSmallest());
        assertEquals(ah.getSmallest(), "b");
        assertTrue(ah.contains("b"));
    }

    @Test
    public void testAdd2() {
        ArrayHeapMinPQ<String> ah = new ArrayHeapMinPQ<>();
        ah.add("c", 3);
        ah.add("i", 9);
        ah.add("g", 7);
        ah.add("d", 4);
//        assertEquals(ah.getItem(2), "d");
        ah.add("a", 1);
        assertEquals(ah.getSmallest(), "a");
//        assertEquals(ah.getItem(2), "c");
        ah.add("h", 8);
        ah.add("e", 5);
//        assertEquals(ah.getItem(3), "e");
        ah.add("b", 2);
//        assertEquals(ah.getItem(8), "i");
//        assertEquals(ah.getItem(2), "b");
//        assertEquals(ah.getItem(4), "c");

    }


    @Test
    public void testChangePriority1() {
        ArrayHeapMinPQ<String> ah = new ArrayHeapMinPQ<>();
        ah.add("a", 1);
        ah.add("d", 4);
        ah.add("c", 3);
        ah.add("b", 2);
        ah.add("e", 5);
        ah.changePriority("a", 6.0);
        assertEquals(ah.getSmallest(), "b");
    }

    @Test
    public void testChangePriority2() {
        ArrayHeapMinPQ<String> ah = new ArrayHeapMinPQ<>();
        ah.add("a", 1);
        ah.add("d", 4);
        ah.add("c", 3);
        ah.add("b", 2);
        ah.add("e", 5);
        ah.changePriority("b", 6.0);
        ah.changePriority("a", 6.0);
        ah.changePriority("d", 1.0);
        assertEquals(ah.getSmallest(), "d");
    }

    @Test
    public void testChangePriority3() {
        ArrayHeapMinPQ<String> ah = new ArrayHeapMinPQ<>();
        ah.add("c", 3);
        ah.add("i", 9);
        ah.add("g", 7);
        ah.add("d", 4);
        ah.add("a", 8);
        ah.add("h", 8);
        ah.add("e", 5);
        ah.add("b", 2);
        ah.add("j", 3);
        ah.add("k", 4);
        ah.changePriority("i", 1);
        assertEquals(1, ah.getIndex("i"));
    }

    @Test
    public void testChangePriority4() {
        ArrayHeapMinPQ<String> ah = new ArrayHeapMinPQ<>();
        ah.add("a", 0);
        ah.add("b", 1);
        ah.add("c", 2);
        ah.add("d", 3);
        ah.add("e", 4);
        ah.add("f", 5);

        ah.changePriority("c", 6);
        assertEquals(ah.getIndex("c"), 6);
        assertEquals(ah.getIndex("f"), 3);
    }

    @Test
    public void testTimeContains() {

        ArrayHeapMinPQ<String> ah = new ArrayHeapMinPQ<>();

        for (int i = 0; i < 2000000; i++) {
            ah.add("a" + i, i + 1);
        }

        Stopwatch sw1 = new Stopwatch();
        ah.contains("a1000");
        System.out.println("Total time elapsed for 2 * 10^6_ArrayHeapMinPQ: "
                + sw1.elapsedTime() + " seconds.");


        Stopwatch sw2 = new Stopwatch();
        NaiveMinPQ<String> na = new NaiveMinPQ<>();
        for (int i = 0; i < 1000000; i++) {
            na.add("a" + i, i + 1);
        }
        na.contains("a1000");
        System.out.println("Total time elapsed for 10^6_NaiveMinPQ: "
                + sw2.elapsedTime() + " seconds.");

    }


    @Test
    public void testAdd() {
        // confirm test correct
        ArrayHeapMinPQ<String> pq = new ArrayHeapMinPQ<>();
        pq.add("c", 3);
        assertEquals("c", pq.priorityQueue[1].item);

        pq.add("i", 9);
        assertEquals("i", pq.priorityQueue[2].item);

        pq.add("g", 7);
        pq.add("d", 4);
        assertEquals("d", pq.priorityQueue[2].item);

        pq.add("a", 1);
        assertEquals("a", pq.priorityQueue[1].item);

        pq.add("h", 8);
        pq.add("e", 5);
        pq.add("b", 2);
        // pq.add("c", 3); throw an error
        // pq.add("d", 4); throw an error
        System.out.println("pq after inserting 10 items: ");
        System.out.println(pq);
        assertEquals(8, pq.size());
        assertEquals("a", pq.priorityQueue[1].item);
        assertEquals("b", pq.priorityQueue[2].item);
        assertEquals("e", pq.priorityQueue[3].item);
        assertEquals("c", pq.priorityQueue[4].item);
        assertEquals("d", pq.priorityQueue[5].item);
        assertEquals("h", pq.priorityQueue[6].item);
        assertEquals("g", pq.priorityQueue[7].item);
        assertEquals("i", pq.priorityQueue[8].item);
    }


    @Test
    public void testInsertAndRemoveOnce() {
        // confirm test correct
        ArrayHeapMinPQ<String> pq = new ArrayHeapMinPQ<>();
        pq.add("c", 3);
        pq.add("i", 9);
        pq.add("g", 7);
        pq.add("d", 4);
        pq.add("a", 1);
        pq.add("h", 8);
        pq.add("e", 5);
        pq.add("b", 2);
        pq.add("j", 3);
        pq.add("k", 4);
        String removed = pq.removeSmallest();
        assertEquals("a", removed);
        assertEquals(9, pq.size());
        assertEquals("b", pq.priorityQueue[1].item);
        assertEquals("c", pq.priorityQueue[2].item);
        assertEquals("e", pq.priorityQueue[3].item);
        assertEquals("j", pq.priorityQueue[4].item);
        assertEquals("d", pq.priorityQueue[5].item);
        assertEquals("h", pq.priorityQueue[6].item);
        assertEquals("g", pq.priorityQueue[7].item);
        assertEquals("i", pq.priorityQueue[8].item);
        assertEquals("k", pq.priorityQueue[9].item);
    }

    @Test
    public void testInsertAndRemoveAllButLast() {
        ArrayHeapMinPQ<String> pq = new ArrayHeapMinPQ<>();
        pq.add("c", 3);
        pq.add("i", 9);
        pq.add("g", 7);
        pq.add("d", 4);
        pq.add("a", 1);
        pq.add("h", 8);
        pq.add("e", 5);
        pq.add("b", 2);
        //pq.add("c", 3);
        //pq.add("d", 4);

        int i = 0;
        String[] expected = {"a", "b", "c", "d", "e", "g", "h", "i"};
        while (pq.size() > 1) {
            assertFalse(pq.contains(pq.removeSmallest()));
            i += 1;
        }
    }

    @Test
    public void testContains() {
        ArrayHeapMinPQ<String> pq = new ArrayHeapMinPQ<>();
        pq.add("c", 3);
        pq.add("i", 9);
        pq.add("g", 7);
        pq.add("d", 4);
        pq.add("a", 1);
        pq.add("h", 8);
        pq.add("e", 5);
        pq.add("b", 2);

        assertEquals(true, pq.contains("c"));
        assertEquals(false, pq.contains("m"));
    }

}

