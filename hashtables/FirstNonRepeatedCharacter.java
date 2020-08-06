package hashtables;

import java.util.Map;
import java.util.HashMap;

/*
*  First non repeated character in a string
*
*  Input = A Green Apple
*
*  Output = G
*/

public final class FirstNonRepeatedCharacter {

	public String nonRepeatedCharacter(String input){
		if(input.isEmpty() || input.length()==1){
			return input;
		}

		var charArray = input.toCharArray();
		final Map<Character, Integer> dict = new HashMap<>(charArray.length);

		for(char ch : charArray){
			if(dict.containsKey(ch)){
				dict.put(ch, dict.get(ch)+1);
			}else{
				dict.put(ch, 1);
			}
		}

		var result = "";
		for(char ch : charArray){
			if(dict.get(ch) == 1){
				result = String.valueOf(ch);
				break;
			}
		}
		return result;
	}

}