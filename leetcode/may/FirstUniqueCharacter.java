package leetcode.may;

import java.util.*;

class CountIndex {
  private int index, count;

  public CountIndex(int index) {
    this.index = index;
    this.count = 1;
  }

  public void setIndex(int index) {
    this.index = index;
  }

  public void setCount(int count) {
    this.count = count;
  }

  public int getIndex() {
    return index;
  }

  public int getCount() {
    return count;
  }
}

public class FirstUniqueCharacter {

  public int firstUniqChar(String s) {
    final Map<Character, CountIndex> charMap = new LinkedHashMap<>(s.length());
    for (int i = 0; i < s.length(); i++) {
      if (charMap.containsKey(s.charAt(i))) {
        CountIndex countIndex = charMap.get(s.charAt(i));
        countIndex.setCount(countIndex.getCount() + 1);
        charMap.put(s.charAt(i), countIndex);
      } else {
        charMap.put(s.charAt(i), new CountIndex(i));
      }
    }

    int index = -1;
    for (Map.Entry<Character, CountIndex> entry : charMap.entrySet()) {
      if (entry.getValue().getCount() == 1) {
        index = entry.getValue().getIndex();
        break;
      }
    }

    return index;
  }

  public int firstUniqCharV2(String s) {
    int res = Integer.MAX_VALUE;

    for (char c = 'a'; c <= 'z'; c++) {
      int index = s.indexOf(c);

      if (index != -1 && index == s.lastIndexOf(c)) res = Math.min(res, index);
    }

    return res == Integer.MAX_VALUE ? -1 : res;
  }
}
