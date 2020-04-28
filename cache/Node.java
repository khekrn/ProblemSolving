package cache;

import java.util.StringJoiner;

public class Node<K, V> {
  private K key;
  private V value;
  private Node next;
  private Node previous;

  private Node(K key, V value) {
    this.key = key;
    this.value = value;
  }

  public static <K, V> Node<K, V> of(K key, V value) {
    return new Node<>(key, value);
  }

  public Node<K, V> getNext() {
    return next;
  }

  public void setNext(Node<K, V> node) {
    this.next = node;
  }

  public Node<K, V> getPrevious() {
    return previous;
  }

  public void setPrevious(Node<K, V> node) {
    this.previous = node;
  }

  public K getKey() {
    return key;
  }

  public void setKey(K key) {
    this.key = key;
  }

  public void setValue(V value) {
    this.value = value;
  }

  public V getValue() {
    return value;
  }

  @Override
  public String toString() {
    return key+" -> "+value;
  }
}
