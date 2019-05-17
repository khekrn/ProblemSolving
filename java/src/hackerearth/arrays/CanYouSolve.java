package arrays;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.Arrays;

public final class CanYouSolve {

	public static void main(String[] args) throws IOException {

		try (BufferedReader reader = new BufferedReader(new InputStreamReader(System.in))) {
			final int N = Integer.parseInt(reader.readLine());

			for (int i = 0; i < N; i++) {
				final int size = Integer.parseInt(reader.readLine());
				int[] arr = new int[size];
				arr = Arrays.stream(reader.readLine().split(" ")).mapToInt(Integer::parseInt).toArray();
				final int max = findMaxV2(arr);

				System.out.println(max);
			}
		}
	}

	public static int findMax(int[] arr) {
		int max = 0;
		for (int i = 0; i < arr.length - 1; i++) {
			for (int j = i + 1; j < arr.length; j++) {

				int temp = Math.abs(arr[i] - arr[j]) + Math.abs(i - j);
				if (temp > max) {
					max = temp;
				}
			}
		}

		return max;
	}

	public static int findMaxV2(int[] arr) {
		int min_val = Integer.MAX_VALUE, max_val = Integer.MIN_VALUE;

		for (int i = 0; i < arr.length-1; i++) {
			
			if ((arr[i] - arr[i+1]) > max_val)
				max_val = arr[i] - arr[i+1];

			if ((i - i+1) < min_val)
				min_val = i - i+1;
		}

		return (max_val + min_val);
	}

}
