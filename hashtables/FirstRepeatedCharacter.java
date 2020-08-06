package hashtables;

import java.util.Set;
import java.util.HashSet;

public final class FirstRepeatedCharacter {

	public String firstRepeatedCharacter(String input){
		var result = "";

		if(input.isEmpty() || input.length() == 1){
			return result;
		}

		var charArray = input.toCharArray();
		final var set = new HashSet<Character>(charArray.length);

		for(char ch : charArray){
			if(set.contains(ch)){
				result = String.valueOf(ch);
				break;
			}
			set.add(ch);
		}

		return result;
	}

}