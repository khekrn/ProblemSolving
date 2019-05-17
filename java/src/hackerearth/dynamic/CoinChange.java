package dynamic;

public final class CoinChange {

	/**
	 * Given an integer representing a given amount of change, write a function to
	 * compute the total number of coins required to make that amount of change. You
	 * can assume that there is always a 1¢ coin
	 **/
	public long getTotalChangesRequired(long n, long[] coins) {
		if (coins.length == 1) {
			return 1;
		}

		long temp = n;
		long res = 0;

		while (temp > 0) {
			for (int i = coins.length - 1; i >= 0; i--) {
				if (coins[i] <= temp) {
					temp = temp - coins[i];
					// System.out.println(temp);
					res++;
				}

				if (temp == 0) {
					break;
				}
			}
		}

		return res;
	}

	final int[] coins = new int[] { 10, 6, 1 };

	public int makeChange(int c) {
		if (c == 0) {
			return 0;
		}

		int minCoins = Integer.MAX_VALUE;
		for (int coin : coins) {
			if (c - coin >= 0) {
				int currentMinCoins = makeChange(c - coin);
				if (currentMinCoins < minCoins)
					minCoins = currentMinCoins;
			}

		}
		//System.out.println(minCoins);
		return minCoins + 1;
	}

	public static void main(String[] args) {
		long[] coins = new long[] { 1, 5, 10, 25 };

		final CoinChange coinChange = new CoinChange();
		System.out.println(coinChange.makeChange(25));
//		System.out.println(coinChange.getTotalChangesRequired(1, coins));
//		System.out.println(coinChange.getTotalChangesRequired(5, coins));
//		System.out.println(coinChange.getTotalChangesRequired(15, coins));
//		System.out.println(coinChange.getTotalChangesRequired(17, coins));
//		System.out.println(coinChange.getTotalChangesRequired(49, coins));
//		System.out.println(coinChange.getTotalChangesRequired(51, coins));
	}

}
