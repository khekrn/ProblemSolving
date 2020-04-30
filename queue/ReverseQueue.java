package queue;

import java.util.*;

/**
 * Reverse a queue values I = [1, 2, 3, 4, 5], O = [5, 4, 3, 2, 1] You are only allowed to use
 * following methods - add() - remove() - isEmpty()
 */
public class ReverseQueue {

  public void reverse(Queue<Integer> queue) {
    var stack = new Stack<Integer>();
    while (!queue.isEmpty()) {
      stack.push(queue.poll());
    }

    while (!stack.isEmpty()) {
      queue.add(stack.pop());
    }
  }
}
