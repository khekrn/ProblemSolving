def generate(numRows: 'int') -> 'List[List[int]]':
    if numRows == 0:
        return [[]]
    if numRows == 1:
        return [[1]]
    if numRows == 2:
        return [[1], [1, 1]]
    res = [[1], [1, 1]]
    for index in range(3, numRows+1):
        previous = res[len(res) - 1]
        new_list = [1] * index
        
        pass
    return res