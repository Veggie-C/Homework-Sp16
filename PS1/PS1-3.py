# CS196 homework problem set 1, file 3/3
#
# You're almost there! The task this time is
# to calculate the slope of a line given two points on that
# line, (x1, y1) and (x2, y2).
#
# Input:
#    x1 - the x-coordinate of the first point (a float)
#    y1 - the y-coordinate of the first point (a float)
#    x2 - the x-coordinate of the second point (a float)
#    y2 - the y-coordinate of the second point (a float)
#
# Output:
#    Return the slope of the line. Do not print anything.
#
# Additional notes:
#    You may assume that the line is not vertical (i.e.,
#    the slope will not be undefined).
#
# Example:
#    slope(5.0, 6.0, 1.0, 2.0) should return 1.0
def slope(x1, y1, x2, y2):
    pass


# Below are some test cases that we have written up for you!
# Feel free to add more to test your code! Though be warned, 
# our grading program will test more cases than this... so make
# sure your functions are correct!
if __name__ == "__main__":
    print "slope(5.0, 6.0, 1.0, 2.0) == " + repr(slope(5., 6., 1., 2.))
    print "slope(1.0, 2.0, 3.0, 4.0) == " + repr(slope(1., 2., 3., 4.))
