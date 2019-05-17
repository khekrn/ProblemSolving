// Given two strings s and t , write a function to determine if t is an anagram of s.

// Example 1:

// Input: s = "anagram", t = "nagaram"
// Output: true
// Example 2:

// Input: s = "rat", t = "car"
// Output: false
// Note:
// You may assume the string contains only lowercase alphabets.

// Follow up:
// What if the inputs contain unicode characters? How would you adapt your solution to such case?

package hashtable

func isAnagram(s string, t string) bool {
    dict := make(map[int32]int)
    
    for _, val := range s {
        dict[val] = dict[val] + 1
    }
    
    for _, val := range t{
        dict[val] = dict[val] - 1
    }
    
    for _, val := range dict {
        if val != 0 {
            return false
        }
    }
    
    return true
}

func isAnagramFast(s string, t string) bool {
	if len(s) != len(t) {
		return false
	}

	arr := make([]int, 128)
	for _, val := range s {
		arr[int(val)]++
	}

	for _, val := range t {
		if arr[int(val)] == 0 {
			return false
		}
		arr[int(val)]--
	}

	return true
}