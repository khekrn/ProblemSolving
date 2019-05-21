package arrays;

import java.util.Arrays;

public final class ArrayManipulation {

	public static long arrayManipulation(int n, int[][] queries) {
		final int[] arr = new int[n];
		;
		for (int[] query : queries) {
			final int startIndex = query[0] - 1;
			final int endIndex = query[1] - 1;
			final int item = query[2];
			for (int i = startIndex; i <= endIndex; i++) {
				int temp = arr[i] + item;
				arr[i] = temp;
			}
		}
		return Arrays.stream(arr).max().getAsInt();
	}

	// Prefix Sum
	static long arrayManipulationV2(int n, int[][] queries) {

		long outputArray[] = new long[n + 2];
		for (int i = 0; i < queries.length; i++) {
			int a = queries[i][0];
			int b = queries[i][1];
			int k = queries[i][2];
			outputArray[a] += k;
			outputArray[b + 1] -= k;
		}
		long max = getMax(outputArray);
		return max;
	}

	private static long getMax(long[] inputArray) {
		long max = Long.MIN_VALUE;
		long sum = 0;
		for (int i = 0; i < inputArray.length; i++) {
			sum += inputArray[i];
			max = Math.max(max, sum);
		}
		return max;
	}

	public static void main(String[] args) {
		final int[][] queries = new int[][] { { 1, 2, 100 }, { 2, 5, 100 }, { 3, 4, 100 } };
		System.out.println(arrayManipulationV2(5, queries));
		
		final int[] arr = new int[] {5, 8, 7, 6, 1, 2, 3};
		final int[] sumArr = new int[arr.length];
		sumArr[0] = arr[0];
		for( int i = 1; i < arr.length; ++i ) 
			sumArr[i] = sumArr[i-1] + arr[i]; 
		System.out.println(Arrays.toString(sumArr));
	}

}
