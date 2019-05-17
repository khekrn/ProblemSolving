package arrays;

public class HourGlass {

	static int hourglassSum(int[][] arr) {
		int max = 0;
		
		int row = arr.length-2;
		int col = arr[0].length-2;
		
		for(int r = 0; r < row; r++) {
			for(int m = 0; m < col; m++) {
				int temp = 0;
				for(int k = m; k < m+3; k++) {
					temp += arr[r][k];
					temp += arr[r+2][k];
				}
				temp += arr[r+1][m+1];
				if (temp > max) {
					max = temp;
				}
				
			}
		}

		return max;
	}

	public static void main(String[] args) {
		final int [][]arr = new int[][] {{1,1,1,0,0,0},
			{0,1,0,0,0,0},
			{1,1,1,0,0,0},
			{0,0,2,4,4,0},
			{0,0,0,2,0,0},
			{0,0,1,2,4,0}};
		
		System.out.println(hourglassSum(arr));
		System.out.println(arr.length);
	}

}
