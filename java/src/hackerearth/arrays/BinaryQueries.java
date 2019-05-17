package arrays;

import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.util.Arrays;

/*

Some problems appear hard though they are very easy. Today Aakash is stuck in a range query problem. He has been given an array with only numbers 0 and 1. There are two types of queries -

0 L R : Check whether the number formed from the array elements L to R is even or odd and print EVEN or ODD respectively. Number formation is the binary number from the bits status in the array L to R

1 X : Flip the Xth bit in the array 

Indexing is 1 based

Input
First line contains a number N and Q as input. Next line contains N space separated 0 or 1. Next Q lines contain description of each query 

Output
Output for only query type 0 L R whether the number in range L to R is "EVEN" or "ODD" (without quotes).

Constraints
1≤ N ≤ 10^6 
1≤ L ≤ R ≤ 10^6 
1≤ Q ≤ 10^6

*/

public class BinaryQueries {
	
	public static void main(String[] args)throws Exception {
		final BufferedReader reader = new BufferedReader(new InputStreamReader(System.in));
		
		String[] arr = reader.readLine().split(" ");
		
		//final int N = Integer.parseInt(arr[0]);
		final int Q = Integer.parseInt(arr[1]);
		
		final String []seqArr = reader.readLine().split(" ");
		
		for(int i = 0; i < Q; i++) {
			String []query = reader.readLine().split(" ");
			if (query.length == 3) {
				int startRange = Integer.parseInt(query[1]);
				int stopRange = Integer.parseInt(query[2]);
				String temp = String.join("", Arrays.stream(seqArr, startRange-1, (stopRange-1)+1).toArray(String[]::new));
				long temp2 = Long.parseLong(temp, 2);
				if((temp2 & 1) == 0) {
					System.out.print("EVEN");
				}else {
					System.out.print("ODD");
				}
				System.out.println();
			}else {
				int index = Integer.parseInt(query[1]) - 1;
				
				if (seqArr[index] == "0") {
					seqArr[index] = "1";
				}else {
					seqArr[index] = "0";
				}
			}
		}
		
		
		
		
	}

}
