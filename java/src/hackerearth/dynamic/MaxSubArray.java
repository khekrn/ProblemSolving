package dynamic;

/**
* created by kkishore
*/


// Find Max sum of contigious sub array
public class MaxSubArray {

	public static void main(String[] args) {
		int []arr = new int[]{-2, 3, 2, -1};
		System.out.println(maxSumSubarray(arr));

	}
	
	public static int maxSumSubarray(int []arr){
		int currentMax = arr[0];
		int maxRes = arr[0];
		for(int i = 1; i < arr.length-1; i++){
			currentMax = Math.max(currentMax + arr[i], arr[i]);
			if(currentMax > maxRes){
				maxRes = currentMax;
			}
		}
		return maxRes;
	}

}
