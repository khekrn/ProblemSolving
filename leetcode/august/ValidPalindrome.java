package leetcode.august;

/*

Given a string, determine if it is a palindrome, considering only alphanumeric characters and ignoring cases.

Note: For the purpose of this problem, we define empty string as valid palindrome.

Example 1:

Input: "A man, a plan, a canal: Panama"
Output: true
Example 2:

Input: "race a car"
Output: false
 

Constraints:

s consists only of printable ASCII characters.

*/

public final class ValidPalindrome{

	public boolean isPalindrome(String s) {
     	StringBuilder sb = new StringBuilder(s.length());
     	for(char c : s.toCharArray()){
     		if(Character.isDigit(c) || Character.isLetter(c)){
     			sb.append(c);
     		}
     	}

     	String input = sb.toString().toLowerCase();
     	int leftIndex = 0;
     	int rightIndex = input.length() - 1;

     	boolean result = true;

     	while(leftIndex < rightIndex){
     		if(input.charAt(leftIndex) != input.charAt(rightIndex)){
     			result = false;
     			break;
     		}
     		leftIndex++;
     		rightIndex--;
     	}
     	return result;
    }

}