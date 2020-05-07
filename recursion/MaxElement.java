package recursion;

/**
 * Find the max element in the array using recursion
 *
 * <p>Input = [5, 1, 7, 2, 3, 9, 4]
 *
 * <p>Output = 9
 */
public class MaxElement {

  public int max(int[] arr) {
    return findMax(arr, arr.length - 1);
  }

  public int findMax(int[] arr, int i) {
    if (i == 0) return arr[i];
    return Math.max(arr[i], findMax(arr, i - 1));
  }
}
