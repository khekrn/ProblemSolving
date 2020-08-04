package leetcode.august;

/**
Given an integer (signed 32 bits), write a function to check whether it is a power of 4.

Example 1:

Input: 16
Output: true
Example 2:

Input: 5
Output: false
Follow up: Could you solve it without loops/recursion?

*/
public final class PowerOfFour {

	/*
		Log4(16) = X

		16 = X ^ 4

		log 4 (16) = log (16) / log (4) = X
	*/
	public boolean isPowerOfFour(int num) {
        if (num == 0){
            return false;
        }
        
        int result = (int) (Math.log(num) / Math.log(4));
        return num == Math.pow(4, result);
    }

}