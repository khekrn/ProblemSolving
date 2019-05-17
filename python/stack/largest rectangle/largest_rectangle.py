def largestRectangle(h):
    max_area = 0
    i = 0
    while i < len(h):
        j = i
        ele = h[i]
        while j < len(h):
            ele = min(ele, h[j])
            max_area = max(max_area, (j-i+1) * ele)
            j += 1
        i += 1
    return max_area

'''
static long largestRectangle(int[] h) {
    Stack<int[]> s = new Stack<>(); // Create stack of span = [x0, x1]
    int n = h.length;
    h = Arrays.copyOf(h, n+1); // Append a sentinel to array h
    int x1;
    int maximum = 0;
    for(int x0 = 0; x0 <= n; x0++) {
        for(x1 = x0; !s.isEmpty() && h[s.peek()[0]] >= h[x0]; ) {
            int[] x = s.pop();
            x1 = x[1];
            maximum = Math.max(maximum, h[x[0]] * (x0 - x1));
        }
        s.push(new int[]{x0, x1});
    }
    return maximum;
}
'''

h = [1, 2, 3, 4, 5]
print(largestRectangle(h))

h = [-1, 8, 4, 2, 14, 3, 8, 9]
print(largestRectangle(h))

h = [11, 11, 10, 10, 10]
print(largestRectangle(h))

h = [1, 3, 5, 9, 11]
print(largestRectangle(h))