# CS196 homework problem set 1, file 2/3
#
# Just one question in this file! Your task is to write
# the algorithm to find the roots of a quadratic equation,
# ax^2 + bx + c = 0.
#
# Input:
#   a - the coefficient of the x^2 term (a float)
#   b - the coefficient of the x term (a float)
#   c - the constant term (a float)
#
# Output:
#   Print the 2 solutions of the quadratic equation, one on each
#   line. Do not return anything. Print them in increasing order.
#
# Additional notes:
#   You may assume that the discriminant is positive (i.e., 
#   there are two real solutions to the problem).
#
# Hint:
#   The square root of x is the same as x raised to the 0.5 power.
#
# Example:
#   solve_quadratic(5.0, 6.0, 1.0) should print:
#     -1.0
#     -0.2
def solve_quadratic(a, b, c):
    pass


# Below are some test cases that we have written up for you!
# Feel free to add more to test your code! Though be warned, 
# our grading program will test more cases than this... so make
# sure your functions are correct!
if __name__ == "__main__":
    print "Running solve_quadratic(5.0, 6.0, 1.0):"
    solve_quadratic(5.0, 6.0, 1.0)

    print "Running solve_quadratic(1.0, 2.0, -8.0):"
    solve_quadratic(1.0, 2.0, -8.0)
