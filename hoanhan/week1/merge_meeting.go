package week1

// Problem:
// Given a list of unsorted, independent Meetings, returns a list of a merged
// one.
//
// Example:
// Given:  []Meeting{{1, 2}, {2, 3}, {4, 5}}
// Return: []Meeting{{1, 3}, {4, 5}}
//

import (
	"fmt"
	"sort"
)

// Meeting struct definition
type Meeting struct {
	Start int
	End   int
}

func (m *Meeting) String() string {
	return fmt.Sprintf("Start : %d, End : %d", m.Start, m.End)
}

// MergeMeetings merges the given Meetings
func MergeMeetings(meetings []Meeting) []Meeting {
	sort.Slice(meetings, func(i int, j int) bool {
		return meetings[i].Start < meetings[j].Start
	})

	fmt.Println(meetings)

	res := make([]Meeting, 0, 0)
	return res
}
