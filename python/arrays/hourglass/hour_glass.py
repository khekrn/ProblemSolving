def hourglassSum(arr):
    rows = len(arr)
    cols = len(arr[0])
    start_row, middle_row, stop_row = 0, 1, 2 
    max_sum = 0
    while start_row < rows and stop_row < rows:
        start_index, middle_index, stop_index = 0, 1, 3
        while start_index < cols and stop_index <= cols:
            head = arr[start_row][start_index:stop_index]
            mid = arr[middle_row][middle_index]
            tail = arr[stop_row][start_index:stop_index]
            current_sum = sum(head) + mid + sum(tail)
            if current_sum > max_sum:
                max_sum = current_sum
            start_index, middle_index, stop_index = start_index + 1, middle_index + 1, stop_index +1
            # res = head + [mid] + tail            
        start_row, middle_row, stop_row = start_row + 1, middle_row + 1, stop_row + 1
    return max_sum

arr = [[1,1,1,0,0,0],[0,1,0,0,0,0],[1,1,1,0,0,0],[0,0,2,4,4,0],[0,0,0,2,0,0],[0,0,1,2,4,0]]
print(hourglassSum(arr))