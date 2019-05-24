package arrays;

import java.util.*;

public class DynamicArrays {

	public static void main(String[] args) {
		final int N = 2;
		final List<List<Integer>> queries = new ArrayList<>();
		queries.add(Arrays.asList(1, 0, 5));
		queries.add(Arrays.asList(1, 1, 7));
		queries.add(Arrays.asList(1, 0, 3));
		queries.add(Arrays.asList(2, 1, 0));
		queries.add(Arrays.asList(2, 1, 1));
		
		final List<Integer> res = dynamicArray(N, queries);
		System.out.println(res);
	}

	public static List<Integer> dynamicArray(int n, List<List<Integer>> queries) {
		final List<List<Integer>> tempList = new ArrayList<>();
		for(int i = 0; i < n; i++) {
			tempList.add(new ArrayList<>());
		}
		final List<Integer> result = new ArrayList<Integer>();
		int lastAnswer = 0;

		for (List<Integer> query : queries) {
			int x = query.get(1);
			int y = query.get(2);
			int seqIndex = (x ^lastAnswer) % n;
			if (query.get(0) == 1) {
				tempList.get(seqIndex).add(y);
			} else {
				int index = y % tempList.get(seqIndex).size();
				lastAnswer = tempList.get(seqIndex).get(index);
				result.add(lastAnswer);
			}
		}
		return result;
	}
}
