package main

import (
	"strings"

	"github.com/khekrn/ps/hackerrank"
)

func main() {
	magazine := strings.Split("two times three is not four", " ")
	notes := strings.Split("two times two is four", " ")
	hackerrank.CheckMagazine(magazine, notes)
}
