# CS196 homework problem set 1, file 3/3
#
# You're almost there! The task this time is to calculate 
# the slope and y-intercept of a line given two points on that
# line, (x1, y1) and (x2, y2).
#
# Input:
#    x1 - the x-coordinate of the first point (a float)
#    y1 - the y-coordinate of the first point (a float)
#    x2 - the x-coordinate of the second point (a float)
#    y2 - the y-coordinate of the second point (a float)
#
# Output:
#    Print the slope of the line on the first line, and the
#    y-intercept of the line on the second line. Do not 
#    return anything. You should only print the numbers; 
#    do not print any other text.
#
# Additional notes:
#    You may assume that the line is not vertical (i.e.,
#    the slope will not be undefined).
#
# Example:
#    line_info(0.0, 4.0, 2.0, 7.0) should print:
#       1.5
#       4.0
def line_info(x1, y1, x2, y2):
    pass


# Below are some test cases that we have written up for you!
# Feel free to add more to test your code! Though be warned, 
# our grading program will test more cases than this... so make
# sure your functions are correct!
if __name__ == "__main__":
    print "Running line_info(0.0, 4.0, 2.0, 7.0):"
    line_info(0.0, 4.0, 2.0, 7.0)
    
    print "Running line_info(1.0, 2.0, 3.0, 4.0):"
    line_info(1.0, 2.0, 3.0, 4.0)
