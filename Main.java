import array.*;
import java.util.Arrays;

public class Main{
	public static void main(String[] ags){
		var agram = new Anagram();
		
		var word1 = "restful";
		var word2 = "fluster";
		
		var isAnagram = agram.isAnagram2(word1, word2);
		System.out.println(isAnagram);

		word1 = "fun";
		word2 = "dead";
		
		isAnagram = agram.isAnagram2(word1, word2);
		System.out.println(isAnagram);
	}
}