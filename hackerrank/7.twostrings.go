package hackerrank

// TwoStrings implementation
// https://www.hackerrank.com/challenges/two-strings/problem?h_l=interview&playlist_slugs%5B%5D=interview-preparation-kit&playlist_slugs%5B%5D=dictionaries-hashmaps
func TwoStrings(s1 string, s2 string) string {
	res := "NO"
	dict := map[rune]struct{}{}

	var nothing struct{}

	for _, item := range s1 {
		if _, exist := dict[item]; !exist {
			dict[item] = nothing
		}
	}

	for _, item := range s2 {
		if _, exist := dict[item]; exist {
			res = "YES"
			break
		}
	}
	return res
}
