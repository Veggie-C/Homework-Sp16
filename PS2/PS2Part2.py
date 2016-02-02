# CS196 homework problem set 2, file 2/4
#
# Reverse factorials
#
# Your task in this file is to complete the function reverse_factorials,
# which will print out the factorial of each integer from 0 to n, in reverse order.
#
# Input:
#   n: an integer
#
# Output:
#   Print each factorial number from n! down to 0!, one number per line.
#   If n is less than zero, print -1. Also note that 0! is equal to 1.
#
# Hint:
#   https://en.wikipedia.org/wiki/Factorial
#
# Example:
#   >>> reverse_factorials(10)
#   3628800
#   362880
#   40320
#   5040
#   720
#   120
#   24
#   6
#   2
#   1
#   1
#
#   >>> reverse_factorials(0)
#   1
#
#   >>> reverse_factorials(-10)
#   -1
def reverse_factorials(n):
    pass


if __name__ == "__main__":
    print "Running reverse_factorials(10):"
    reverse_factorials(10)
    print "Expected output:"
    print "3628800\n362880\n40320\n5040\n720\n120\n24\n6\n2\n1\n1"
