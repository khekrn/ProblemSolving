package hackerrank

// SockMerchant implementation
// https://www.hackerrank.com/challenges/sock-merchant/problem?h_l=interview&playlist_slugs%5B%5D=interview-preparation-kit&playlist_slugs%5B%5D=warmup
func SockMerchant(n int32, ar []int32) int32 {
	if n == 0 {
		return 0
	}

	pairs := make([]int32, 0, 0)
	set := make(map[int32]struct{})

	var nothing struct{}

	for i := 0; i < len(ar); i++ {
		if _, ok := set[ar[i]]; ok {
			pairs = append(pairs, ar[i])
			delete(set, ar[i])
		} else {
			set[ar[i]] = nothing
		}
	}
	return int32(len(pairs))
}
