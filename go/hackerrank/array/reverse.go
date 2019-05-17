package array

/*

An array is a type of data structure that stores elements of the same type in a contiguous block of memory. In an array, A , of size N,
each memory location has some unique index, i (where 0 <= i < N), that can be referenced as  A[i].

Given an array, A , of N integers, print each element in reverse order as a single line of space-separated integers.

Note: If you've already solved our C++ domain's Arrays Introduction challenge, you may want to skip this.

Input Format

The first line contains an integer, N (the number of integers in ).
The second line contains N space-separated integers describing .

Constraints

- 1 <= N <= 10^3
- 1 <= A[i] <= 10^4, where A[i] is the ith integer in A

Output Format

Print all N integers in A in reverse order as a single line of space-separated integers.

*/

// ReverseArray return's reverse array
func ReverseArray(arr []int32) []int32 {
	size := len(arr)
	res := make([]int32, size, size)
	for i, j := size-1, 0; i >= 0; i, j = i-1, j+1 {
		res[j] = arr[i]
	}
	return res
}
