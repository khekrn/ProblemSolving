package hackerrank

import "strings"

// RepeatedString implementation
// https://www.hackerrank.com/challenges/repeated-string/problem?h_l=interview&playlist_slugs%5B%5D=interview-preparation-kit&playlist_slugs%5B%5D=warmup
func RepeatedString(s string, n int64) int64 {
	if len(s) == 1 {
		return n
	}

	numberOfa := int64(strings.Count(s, "a"))
	numOfRepeatWord := int64(n / int64(len(s)))
	remainWord := int64(n % int64(len(s)))
	numberOfaRemainWord := int64(strings.Count(s[:remainWord], "a"))
	return int64(numberOfa*numOfRepeatWord + numberOfaRemainWord)
}
