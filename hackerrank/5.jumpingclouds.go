package hackerrank

// JumpingOnClouds implementation
// https://www.hackerrank.com/challenges/jumping-on-the-clouds/problem?h_l=interview&playlist_slugs%5B%5D=interview-preparation-kit&playlist_slugs%5B%5D=warmup
func JumpingOnClouds(c []int32) int32 {
	count := -1
	for i := 0; i < len(c); i, count = i+1, count+1 {
		if i < len(c)-2 && c[i+2] == 0 {
			i++
		}
	}
	return int32(count)
}
