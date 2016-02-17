# CS196 homework problem set 4, file 3/4
#
# Selection sort
#
# Your job for this task is to implement selection sort! The algorithm
# is as follows: For each index (i) in the list (0 to len(list) - 1), find
# the smallest item in the portion of the list after that index
# (i + 1 to len(list) - 1), and swap the smallest and current items if the
# smallest item is less than the current item. Then move to the next index
# (i = i + 1) and repeat the process.
#
# Input:
#   x: a list of integers
#
# Output: None (don't return anything, you should directly modify the input list)
#
# Example:
#   >>> a = [1, 7, 3, 6, 1, 8, 9, 2]
#   >>> selection_sort(a)
#   >>> print a
#   [1, 1, 2, 3, 6, 7, 8, 9]
def selection_sort(x):
    pass


if __name__ == "__main__":
    def check(output, expected):
        if output != expected:
            return "FAILED!"
        else:
            return "PASSED!"

    a = [1, 7, 3, 6, 1, 8, 9, 2]
    print "Before: a = " + str(a)
    selection_sort(a)
    print "After:  a = " + str(a)
    print check(a, [1, 1, 2, 3, 6, 7, 8, 9])
