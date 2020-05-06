package array;

import java.util.Arrays;

public class MergeSortedArray {
  public void merge(int[] nums1, int m, int[] nums2, int n) {
    System.arraycopy(nums2, 0, nums1, m - n, n);
  }

  public static void main(String[] ads) {
    var obj = new MergeSortedArray();
    var nums1 = new int[] {1, 2, 3, 0, 0, 0};
    var nums2 = new int[] {2, 5, 6};
    var start = System.currentTimeMillis();
    obj.merge(nums1, nums1.length, nums2, nums2.length);
    var duration = System.currentTimeMillis() - start;
    System.out.println("Time = " + duration);
    System.out.println(Arrays.toString(nums1));
  }
}
