def gridlandMetro(n, m, k, track):
    total_lamp_post = n * m
    n_track = 0
    previous_row, previous_c1, previous_c2 = 0,0,0
    for row in track:
        r,c1,c2 = row[0], row[1], row[2]                    
        print(r, c1, c2)
        previous_row, previous_c1, previous_c2 = r, c1, c2
    pass


n,m,k = 4,4,3
track = [[4, 4, 3], [2, 2, 3], [3,1,4],[4,4,4]]

gridlandMetro(n, m, k, track)