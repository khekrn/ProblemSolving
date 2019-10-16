package week1

// Given a list of string, reverse its order.
// Given: []string{“a”, “b”, “c”, “d”}
// Return: []string{“d”, “c”, “b”, “a”}

// Reverse function
func Reverse(input []string) []string {
	size := len(input)
	out := make([]string, 0, size)
	for i, j := size-1, 0; i >= 0; i, j = i-1, j+1 {
		//out[j] = input[i]
		out = append(out, input[i])
	}
	return out

}
