# CS196 homework problem set 3, file 3/5
#
# It's Like a Sum, but Not
#
# Given a list of numbers, build a list containing the sum of each number in
# the input list, except the number at the current index.
# 
# As an added challenge (just for fun, no bonus points), try using only one
# for-loop and call the sum() function exactly once, outside the for-loop.
#
# Input:
#   x: a list of numbers
#
# Output:
#   Return the list containing the sums.
#
# Example:
#   >>> sum_except_index([3, 1, 4])
#   [5, 7, 4] <-- This is calculated by [1 + 4, 3 + 4, 3 + 1]
def sum_except_index(x):
    pass


if __name__ == "__main__":
    def check(output, expected):
        if output != expected:
            return "FAILED!"
        else:
            return "PASSED!"

    print "sum_except_index([3, 1, 4]): " + check(sum_except_index([3, 1, 4]), [5, 7, 4])
