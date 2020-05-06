package leetcode.may;

import java.util.HashMap;
import java.util.Map;

/**
 * Given an array of size n, find the majority element. The majority element is the element that
 * appears more than ⌊ n/2 ⌋ times. You may assume that the array is non-empty and the majority
 * element always exist in the array. Example 1:
 *
 * <p>Input: [3,2,3] Output: 3 Example 2:
 *
 * <p>Input: [2,2,1,1,1,2,2] Output: 2
 */
public class MajorityElement {
  public int majorityElement(int[] nums) {
    int maxElement = nums[0];
    int maxCount = 0;

    Map<Integer, Integer> map = new HashMap<>();
    for (int num : nums) {
      if (map.containsKey(num)) {
        int newCount = map.get(num) + 1;
        map.put(num, newCount);
        if (newCount > maxCount) {
          maxCount = newCount;
          maxElement = num;
        }
      } else {
        map.put(num, 1);
      }
    }
    return maxElement;
  }
}
