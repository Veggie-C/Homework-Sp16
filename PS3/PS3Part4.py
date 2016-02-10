# CS196 homework problem set 3, file 4/5
#
# Merge two lists in order
#
# This method is a tough one. Merge two pre-sorted lists into one
# larger sorted list. You MAY NOT use any built-in sorting functions from
# Python (sorted(), list.sort(), etc). Violation of this rule will
# earn you a zero!
# 
# Warning: The lists may have duplicate entries, and do not necessarily
# have the same lengths! Be sure to handle these cases correctly!
# 
# Input:
#   first_list: the first pre-sorted list to merge
#   second_list: the second pre-sorted list to merge
#
# Output:
#   Return a list with all elements from both input lists, sorted in
#   increasing order.
#
# Example:
#   >>> merge_lists_in_order([1, 4, 5, 6], [2, 3, 6])
#   [1, 2, 3, 4, 5, 6, 6]
def merge_lists_in_order(first_list, second_list):
    pass


if __name__ == '__main__':
    def check(output, expected):
        if output != expected:
            return "FAILED!"
        else:
            return "PASSED!"

    print "merge_lists_in_order([1, 4, 5, 6], [2, 3, 6]): " + check(
        merge_lists_in_order([1, 4, 5, 6], [2, 3, 6]),
        [1, 2, 3, 4, 5, 6, 6]
    )
