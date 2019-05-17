package arrays;

import java.util.Arrays;

public class ReverseArray {

	public static void main(String[] args) {
		final int[] arr = new int[] {1, 2, 3, 4};
		System.out.println(Arrays.toString(reverseArray(arr)));
	}
	
	public static int[] reverseArray(int []arr) {
		final int []res = new int[arr.length];
		int j = 0;
		for(int i = arr.length-1; i >= 0; i--) {
			res[j] = arr[i];
			j++;
		}
		return res;
	}

}
