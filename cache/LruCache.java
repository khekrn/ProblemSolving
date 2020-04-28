package cache;

import java.util.*;
import java.util.stream.Collectors;
import java.util.stream.StreamSupport;

/**
 * @author khekrn
 *     <p>Implementation of LRU Cache
 */
public class LruCache<K, V> implements Iterable<Node<K, V>> {

  private final int capacity;
  private final Map<K, Node<K, V>> lru;

  private int size;
  private Node<K, V> head;
  private Node<K, V> tail;

  private LruCache(int capacity) {
    this.capacity = capacity;
    this.lru = new HashMap<>(capacity);
  }

  public static <K, V> LruCache<Integer, String> of(int capacity) {
    return new LruCache<>(capacity);
  }

  private void delete(Node<K, V> node) {

    if (node.getPrevious() != null) {
      node.getPrevious().setNext(node.getNext());
    } else {
      head = node.getNext();
    }

    if (node.getNext() != null) {
      node.getNext().setPrevious(node.getPrevious());
    } else {
      tail = node.getPrevious();
    }
  }

  private void setHead(Node<K, V> node) {
    node.setNext(head);
    node.setPrevious(null);

    if (head != null) {
      head.setPrevious(node);
    }

    head = node;

    if (tail == null) {
      tail = head;
    }
  }

  public void insert(K key, V value) {
    if (lru.containsKey(key)) {
      var currentNode = lru.get(key);
      currentNode.setValue(value);
      delete(currentNode);
      setHead(currentNode);
    } else {
      var newNode = Node.of(key, value);
      if (size == capacity) {
        lru.remove(tail.getKey());
        delete(tail);
        size--;
      }
      setHead(newNode);
      lru.put(key, newNode);
      size++;
    }
  }

  public V get(K key) {
    V result = null;
    if (lru.containsKey(key)) {
      var currentNode = lru.get(key);
      delete(currentNode);
      setHead(currentNode);
      result = currentNode.getValue();
    }
    return result;
  }

  public int size() {
    return size;
  }

  public String toString() {
    return StreamSupport.stream(
            Spliterators.spliteratorUnknownSize(this.iterator(), Spliterator.ORDERED), false)
        .map(Node::toString)
        .collect(Collectors.joining(", "));
  }

  public Iterator<Node<K, V>> iterator() {
    return new Iterator<>() {

      private Node<K, V> currentNode = head;

      public boolean hasNext() {
        return currentNode != null;
      }

      public Node<K, V> next() {
        var temp = currentNode;
        currentNode = currentNode.getNext();
        return temp;
      }
    };
  }
}
