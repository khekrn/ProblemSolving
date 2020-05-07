package recursion;

/**
 * Find whether the given string is Palindrome or not
 *
 * <p>Input = "malayalam"
 *
 * <p>Output = true
 *
 * <p>Input "fun"
 *
 * <p>Output = false
 */
public class Palindrome {

  public boolean isPalindrome(String word) {
    return isPalindrome(word, 0, word.length() - 1);
  }

  private boolean isPalindrome(String word, int i, int j) {
    if (i >= j) return true;
    return word.charAt(i) == word.charAt(j) && isPalindrome(word, i + 1, j - 1);
  }
}
