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
	
	static int hourglassV2(int [][]arr) {
		int max = Integer.MIN_VALUE;
		int rows = arr.length;
		int cols = arr[0].length;
		
		for(int i = 0; i < rows - 2; i++ ){
			for(int j = 0; j < cols -2; j++){
				int sum = (arr[i][j] + arr[i][j+1] + arr[i][j+2]) + (arr[i+1][j+1]) + (arr[i+2][j] +
						arr[i+2][j+1] + arr[i+2][j+2]);
				if (sum > max) {
					max = sum;
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
		
		System.out.println(hourglassV2(arr));
		System.out.println(arr.length);
	}

}
