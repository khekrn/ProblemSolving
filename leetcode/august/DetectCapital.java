package leetcode.august;

/**
 * 
 * Given a word, you need to judge whether the usage of capitals in it is right
 * or not.
 * 
 * We define the usage of capitals in a word to be right when one of the
 * following cases holds:
 * 
 * All letters in this word are capitals, like "USA". All letters in this word
 * are not capitals, like "leetcode". Only the first letter in this word is
 * capital, like "Google". Otherwise, we define that this word doesn't use
 * capitals in a right way.
 * 
 * 
 * Example 1:
 * 
 * Input: "USA" Output: True
 * 
 * 
 * Example 2:
 * 
 * Input: "FlaG" Output: False
 * 
 * 
 * Note: The input will be a non-empty word consisting of uppercase and
 * lowercase latin letters.
 * 
 */
public final class DetectCapital {

	public boolean detectCapitalUse(String word) {
		if(word.length() == 1){
			return true;
		}
		char[] arr = word.toCharArray();
		if(Character.isUpperCase(arr[0]) && Character.isLowerCase(arr[1])){
			return isValid(arr, 1, 97, 122);
		}
		return Character.isUpperCase(arr[0]) ? isValid(arr, 0, 65, 90) : isValid(arr, 0, 97, 122);
	}

	private boolean isValid(char[] arr, int index, int startValue, int endValue) {
		boolean result = true;
		for (int i = index; i < arr.length; i++) {
			int temp = (int) arr[i];
			if (temp < startValue || temp > endValue) {
				result = false;
			}
		}
		return result;
	}

}