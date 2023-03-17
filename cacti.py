def cacti_number(plot):
    row = len(plot)
    col = len(plot[0])
    count = 0
    for i in range(row):
        for j in range(col):
            if plot[i][j] == 0:
                if (i == 0 or plot[i-1][j] == 0) and \
                    (j == 0 or plot[i][j-1] == 0) and \
                    (i == row - 1 or plot[i+1][j] == 0) and \
                    (j == col -1 or plot[i][j+1] == 0) and \
                    (i == 0 or j == 0 or plot[i-1][j-1] == 0) and \
                    (i == row - 1 or j == 0 or plot[i+1][j-1] == 0) and \
                    (i == row - 1 or j == col - 1 or plot[i+1][j+1] == 0) and \
                    (i == 0 or j == col - 1 or plot[i-1][j+1] == 0):
                    count+=1
    return count


plot = [ [1, 0, 0, 1, 0],
         [0, 1, 0, 0, 0],
         [1, 0, 0, 0, 0] ]
print(cacti_number(plot))