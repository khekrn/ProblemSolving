package hashtable

func Intersection(nums1 []int, nums2 []int) []int {
	set := make(map[int]struct{})
	var nothing struct{}
	for i := 0; i < len(nums1); i++ {
		if _, exist := set[nums1[i]]; !exist {
			set[nums1[i]] = nothing
		}
	}

	set2 := make(map[int]struct{})
	res := make([]int, 0)
	for i := 0; i < len(nums2); i++ {
		if _, exist := set2[nums2[i]]; !exist {
			if _, setExist := set[nums2[i]]; setExist {
				res = append(res, nums2[i])
			}
			set2[nums2[i]] = nothing
		}
	}
	return res
}
