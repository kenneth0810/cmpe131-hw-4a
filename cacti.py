def cacti_number(plot):
    row = len(plot) # how many sub-lists
    col = len(plot[0]) # how many elements in the sub-list
    count = 0

    if row == 1 and col > 1: # if 1 row and multiple col
        for i in range(col):
            if plot[0][i] == 0:
                if (i == 0 and plot[0][i+1] == 0) or (i == col - 1 and plot[0][i-1] == 0): # if leftmost or rightmost spot
                    plot[0][i] = 1
                    count+=1
                else: # if middle of the row
                    if plot[0][i-1] == 0 and plot[0][i+1] == 0:
                        plot[0][i] = 1
                        count += 1
    elif row > 1 and col == 1: # if 1 col and multiple row
        for i in range(row):
            if plot[i][0] == 0:
                if (i == 0 and plot[i+1][0] == 0) or (i == row - 1 and plot[i-1][0] == 0): # if top or bottom spot
                    plot[i][0] = 1
                    count+=1
                else: # if middle of the col
                    if plot[i-1][0] == 0 and plot[i+1][0] == 0:
                        plot[i][0] = 1
                        count += 1
    elif row > 1 and col > 1: # if multiple row and col
        for i in range(row):
            for j in range(col):
                if plot[i][j] == 0:
                    if i == 0: # if top row
                        if (j == 0 and plot[i][j+1] == 0 and plot[i+1][j] == 0) or (j == col - 1 and plot[i][j-1] == 0 and plot[i+1][j] == 0): # if left or right corner
                            plot[i][j] = 1
                            count += 1
                        else: # if middle of top row
                            if (j != 0 and plot[i][j-1] == 0 and plot[i][j+1] == 0 and plot[i+1][j] == 0):
                                plot[i][j] = 1
                                count += 1
                    elif i == row - 1: # if bottom row
                        if (j == 0 and plot[i][j+1] == 0 and plot[i-1][j] == 0) or (j == col - 1 and plot[i][j-1] == 0 and plot[i-1][j] == 0): # if left or right corner
                            plot[i][j] = 1
                            count += 1
                        else: # if middle of bottom row
                            if (j != 0 and plot[i][j-1] == 0 and plot[i][j+1] == 0 and plot[i-1][j] == 0):
                                plot[i][j] = 1
                                count += 1
                    elif j == 0 and (i != 0 and i != row - 1): # if middle of first column
                        if (plot[i+1][j] == 0 and plot[i-1][j] == 0 and plot[i][j+1] == 0):
                            plot[i][j] = 1
                            count += 1
                    elif j == col - 1 and (i !=0 and i != row - 1): # if middle of last column
                        if (plot[i+1][j] == 0 and plot[i-1][j] == 0 and plot[i][j-1] == 0):
                            plot[i][j] = 1
                            count += 1
                    else: # if somewhere in the middle of the plot
                        if (plot[i+1][j] == 0 and plot[i-1][j] == 0 and plot[i][j+1] == 0 and plot[i][j-1] == 0): # check all sides
                            plot[i][j] = 1
                            count += 1
    else: # if 1 row, 1 col
        if plot[0][0] == 0:
            count += 1

    return count


# plot = [ [1, 1, 1, 1, 1],
#          [0, 0, 0, 0, 0],
#          [0, 1, 0, 1, 0] ]

plot = [[1]]

print(cacti_number(plot))