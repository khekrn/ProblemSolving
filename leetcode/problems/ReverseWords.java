package leetcode.problems;

/**
 * Given an input string, reverse the string word by word. 

Example 1:

Input: "the sky is blue"
Output: "blue is sky the"
Example 2:

Input: "  hello world!  "
Output: "world! hello"
Explanation: Your reversed string should not contain leading or trailing spaces.
Example 3:

Input: "a good   example"
Output: "example good a"
Explanation: You need to reduce multiple spaces between two words to a single space in the reversed string.
 

Note:

A word is defined as a sequence of non-space characters.
Input string may contain leading or trailing spaces. However, your reversed string should not contain leading or trailing spaces.
You need to reduce multiple spaces between two words to a single space in the reversed string.
 */

public class ReverseWords {

    public String reverseWords(String s) {
        if(s.length() == 0 || s.equals(" ")){
            return s.trim();
        }
        String[] words = s.split(" ");
        if(words.length == 0){
            return "";
        }

        StringBuilder sb = new StringBuilder(words.length);
        for(int i = words.length-1; i>=0; i--){
            if(words[i].length()!=0){
                sb.append(words[i]).append(" ");
            }
        }
        sb.deleteCharAt(sb.length()-1);
        return sb.toString().trim();
    }
    
}