package arrays;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.HashMap;
import java.util.Map;

public class MemoriseMe {
	
	public static void main(String[] args) throws IOException {				
		try(final BufferedReader reader = new BufferedReader(new InputStreamReader(System.in))) {
			final int total = Integer.parseInt(reader.readLine());
			final String inputList = reader.readLine();						
			
			String[] split = inputList.split(" ");
			
			final Map<Integer, Integer> hashMap = new HashMap<>(total);
			
			for(int i = 0; i < split.length; i++) {
				final int temp = Integer.parseInt(split[i]);
				if(hashMap.containsKey(temp)) {
					hashMap.put(temp, hashMap.get(temp) + 1);
				}else {
					hashMap.put(temp, 1);
				}
			}
			
			final int totalInputs = Integer.parseInt(reader.readLine());
			
			for(int i = 0; i < totalInputs; i++) {
				final int temp = Integer.parseInt(reader.readLine());
				if(hashMap.containsKey(temp)) {
					System.out.println(hashMap.get(temp));
				}else {
					System.out.println("NOT PRESENT");
				}
			}
		}		

	}

}
