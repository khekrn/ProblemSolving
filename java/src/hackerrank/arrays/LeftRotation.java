package arrays;

import java.util.Arrays;

public class LeftRotation {
	
	public static void leftRotate(int []array, int n) {
		for(int i = 0; i < n; i++) {
			int temp = array[0];
			System.arraycopy(array, 1, array, 0, array.length-1);
			array[array.length-1] = temp;
		}
	}
	
	/**
	 * Implementing array rotation using Block Swap Algorithm
	 * Step 1: Divide the array into two parts : A[0..k-1] A[k...L-1] where L is length
	 * Step 2: Rotate A[0...k-1] keeping the remaining array same.
	 * Step 3: Rotate A[k....L-1] keeping first part same.
	 * Step 4: Rotate A. 
	 * @param array
	 * @param n
	 */
	public static void leftRotateV2(int []arr, int n) {
		blockSwap(arr, 0, n-1);
		blockSwap(arr, n, arr.length-1);
		blockSwap(arr, 0, arr.length-1);
	}
	
	private static void blockSwap(int []arr, int start, int end) {
		int temp = 0;
		while(start < end) {
			temp = arr[start];
			arr[start] = arr[end];
			arr[end] = temp;
			
			start++;
			end--;
		}
	}
	
	

	public static void main(String[] args) {
		// TODO Auto-generated method stub
		int[] arr = new int[] {1, 2, 3, 4, 5};
		//leftRotate(arr, 4);
		//System.out.println(Arrays.toString(arr));
		leftRotateV2(arr, 4);
		System.out.println(Arrays.toString(arr));
	}

}
