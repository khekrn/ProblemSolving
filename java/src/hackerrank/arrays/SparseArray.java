package arrays;

import java.util.Arrays;
import java.util.Map;
import java.util.function.Function;
import java.util.stream.Collectors;

public final class SparseArray {

	public static int[] matchingStrings(String[] strings, String[] queries) {
		final var dataList = Arrays.asList(strings);
		final var res = Arrays.stream(queries)
				.map(item -> dataList.stream().filter(dataElement -> dataElement.equals(item)).count())
				.mapToInt(x -> x.intValue()).toArray();
		return res;
	}

	public static int[] matchingStringsV2(String[] strings, String[] queries) {

		final Map<String, Long> dict = Arrays.stream(strings)
				.collect(Collectors.groupingBy(Function.identity(), Collectors.counting()));
		final int[] res = Arrays.stream(queries).mapToInt(query -> {
			if (dict.containsKey(query)) {
				return dict.get(query).intValue();
			}
			return 0;
		}).toArray();

		return res;
	}

	public static void main(String[] args) {
		String[] data = new String[] { "aba", "baba", "aba", "xzxb" };
		String[] queries = new String[] { "aba", "xzxb", "ab" };

		int[] res = matchingStringsV2(data, queries);
		System.out.println(Arrays.toString(res));
	}

}
