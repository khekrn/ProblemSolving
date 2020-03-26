package array;

import java.util.Arrays;
import java.util.Map;
import java.util.HashMap;

/**
 * 
 * @author khekrn
 * 
 * Determine whether the two word is anagram or not
 *
 */

public class Anagram {

	// O(N Log N)
	public boolean isAnagram(String word1, String word2){
		if(word1.length() != word2.length()){
			return false;
		}
		var anagram = true;

		var text1 = word1.toCharArray();
		var text2 = word2.toCharArray();

		// O(N Log N)
		Arrays.sort(text1);
		Arrays.sort(text2);

		// O(N)
		for(int i =0; i < text1.length; i++){
			if(text1[i] != text2[i]){
				anagram = false;
				break;
			}
		}

		return anagram;
	}

	//
	public boolean isAnagram2(String word1, String word2){
		if(word1.length() != word2.length()){
			return false;
		}

		var isAnagram = true;

		var text1 = word1.toCharArray();
		var text2 = word2.toCharArray();

		var dict = new HashMap<Character, Integer>(text1.length);

		for(char ch : text1){
			if(dict.containsKey(ch)){
				var value = dict.get(ch);
				dict.put(ch, value++);
			}else{
				dict.put(ch, 1);
			}
		}

		for(char ch : text2){
			if(!dict.containsKey(ch)){
				isAnagram = false;
				break;
			}else{
				var value = dict.get(ch);
				value--;
				if(value < 0){
					isAnagram = false;
					break;
				}else{
					dict.put(ch, value);
				}
			}
		}

		return isAnagram;
	}
}