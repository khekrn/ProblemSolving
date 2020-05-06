package array;

/**
 * Given a binary array, find the maximum number of consecutive 1s in this array.
 *
 * <p>Example 1: Input: [1,1,0,1,1,1] Output: 3 Explanation: The first two digits or the last three
 * digits are consecutive 1s. The maximum number of consecutive 1s is 3. Note:
 *
 * <p>The input array will only contain 0 and 1. The length of input array is a positive integer and
 * will not exceed 10,000
 */
public class MaxConsecutiveOnes {
  public int findMaxConsecutiveOnes(int[] nums) {
    int maxConsecutive = 0;
    int counter = 0;
    for (int num : nums) {
      if (num != 1) {
        counter = 0;
      } else {
        counter++;
      }

      if (maxConsecutive < counter) {
        maxConsecutive = counter;
      }
    }

    return maxConsecutive;
  }
}
