package recursion;

public class SumOfDigits {

  public int sumOfDigits(int digits) {
    return sumOfDigits(digits, 0);
  }

  public int sumOfDigits(int n, int sum) {
    if (n == 0) return sum;
    return sumOfDigits(n / 10, sum + (n % 10));
  }

  public static void main(String[] ags) {
    SumOfDigits obj = new SumOfDigits();
    System.out.println(obj.sumOfDigits(1));
  }
}
