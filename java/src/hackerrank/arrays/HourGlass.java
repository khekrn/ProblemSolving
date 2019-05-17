package arrays;

import java.util.Arrays;

public class HourGlass {

	static int hourglassSum(int[][] arr) {
		int max = 0;
		
		int row = arr.length-2;
		int col = arr[0].length-2;
		
		for(int r = 0; r < row; r++) {
			int midIndex = 1;
			int bottomIndex = 2;
			int temp = 0;
			
			for(int k = 0; k < 2; k++) {
				int colIndex = k + 3;
				
			}
			
//			for(int c = 0; c < colIndex; c++) {
//				temp += arr[r][c];
//			}
			
			temp += arr[r+1][midIndex];
			
			
			
			
			
			if (temp > max) {
				max = temp;
			}
		}

		return max;
	}

	public static void main(String[] args) {
		final int [][]arr = new int[][] {{1,1,1,0,0,0},
			{0,1,0,0,0,0},
			{1,1,1,0,0,0},
			{0,0,0,0,0,0},
			{0,0,0,0,0,0},
			{0,0,0,0,0,0}};
		
		hourglassSum(arr);
		System.out.println(arr.length);
	}

}
