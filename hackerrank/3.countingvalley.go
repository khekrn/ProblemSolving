package hackerrank

// CountingValleys implementation
// https://www.hackerrank.com/challenges/counting-valleys/problem?h_l=interview&playlist_slugs%5B%5D=interview-preparation-kit&playlist_slugs%5B%5D=warmup
func CountingValleys(n int32, s string) int32 {
	nvalleys := 0
	level := 0

	for i := 0; i < len(s); i++ {
		if s[i] == 'U' {
			level++
		} else if s[i] == 'D' {
			level--
		}

		if level == 0 && s[i] == 'U' {
			nvalleys++
		}

	}

	return int32(nvalleys)
}
