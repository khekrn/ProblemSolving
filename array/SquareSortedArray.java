package array;

import java.util.Arrays;

public class SquareSortedArray {

  public int[] sortedSquares(int[] A) {
    return Arrays.stream(A).map(num -> num * num).sorted().toArray();
  }
}
