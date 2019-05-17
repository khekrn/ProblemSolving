package array

// Given a matrix A, return the transpose of A.

// The transpose of a matrix is the matrix flipped over it's main diagonal, switching the row and column indices of the matrix.

// Example 1:

// Input: [[1,2,3],[4,5,6],[7,8,9]]
// Output: [[1,4,7],[2,5,8],[3,6,9]]
// Example 2:

// Input: [[1,2,3],[4,5,6]]
// Output: [[1,4],[2,5],[3,6]]

// Note:

// 1 <= A.length <= 1000
// 1 <= A[0].length <= 1000

func Transpose(A [][]int) [][]int {
	rowSize := len(A)
	colSize := len(A[0])
	res := [][]int{}
	j := 0
	for j < colSize {
		i := 0
		row := make([]int, rowSize)
		for i < rowSize {
			row[i] = A[i][j]
			i++
		}
		res = append(res, row)
		j++
	}
	return res
}

func TransposeV2(A [][]int) [][]int {
	rows, cols := len(A[0]), len(A)
	res := make([][]int, rows)
	for i := 0; i < rows; i++ {
		res[i] = make([]int, cols)
	}
	for i := 0; i < rows; i++ {
		for j := 0; j < cols; j++ {
			res[i][j] = A[j][i]
		}
	}
	return res
}
