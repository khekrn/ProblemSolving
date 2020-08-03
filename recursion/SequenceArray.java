package recursion;

public class SequenceArray {

  public boolean isSequenceArray(int[] arr) {
    return arr.length == 1 ? true : isSequenceArray(arr, 1, 0);
  }

  public boolean isSequenceArray(int[] arr, int currentIndex, int previousIndex) {
    if (currentIndex == arr.length) return true;
    if (arr[previousIndex] + 1 != arr[currentIndex]) {
      return false;
    }
    return isSequenceArray(arr, currentIndex + 1, previousIndex + 1);
  }
}
