package array;

/**
 * @author khekrn
 *     <p>Reverse array in place
 */
public class ReverseArray {

  public int[] reverseArray(int[] arr) {
    if (arr.length > 0) {
      var leftIndex = 0;
      var rightIndex = arr.length - 1;
      while (leftIndex <= rightIndex) {
        var temp = arr[leftIndex];
        arr[leftIndex] = arr[rightIndex];
        arr[rightIndex] = temp;

        leftIndex++;
        rightIndex--;
      }
    }
    return arr;
  }
}
