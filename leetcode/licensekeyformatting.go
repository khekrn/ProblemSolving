package leetcode

import (
	"bytes"
)

// LicenseKeyFormatting https://leetcode.com/problems/license-key-formatting/
func LicenseKeyFormatting(S string, K int) string {
	var buffer bytes.Buffer

	runes := []rune(S)
	counter := 0
	firstHyphen := false
	for i := 0; i < len(runes); i++ {
		if runes[i] == '-' {
			if !firstHyphen {
				firstHyphen = true
				buffer.WriteRune(runes[i])
				counter = 0
				continue
			}

			if counter == K {
				counter = 0
				buffer.WriteRune(runes[i])
			}
		} else {
			counter++
			buffer.WriteRune(runes[i])
		}
	}

	return buffer.String()
}
