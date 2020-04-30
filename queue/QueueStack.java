package queue;

import java.util.*;

/** Implement queue using Stack */
public class QueueStack {

  private Stack<Integer> s1 = new Stack<>();
  private Stack<Integer> s2 = new Stack<>();

  // O(1)
  public void enqueue(Integer item) {
    s1.push(item);
  }

  // O(N)
  public Integer dequeue() throws Exception {
    if (isEmpty()) {
      throw new Exception("Queue is Empty");
    }
    if (s2.isEmpty()) {
      while (!s1.isEmpty()) {
        s2.push(s1.pop());
      }
    }
    return s2.pop();
  }

  public Integer peek() {
    return s2.peek();
  }

  public boolean isEmpty() {
    return s1.isEmpty() && s2.isEmpty();
  }

  public int size() {
    return s1.size() + s2.size();
  }
}
