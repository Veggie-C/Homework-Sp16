# CS196 homework problem set 3, file 5/5

# List zipper
# 
# Given two lists, create a list where each element in the
# new list is a tuple consisting of the corresponding
# elements in each list.
# 
# If one list is longer than the other, return an empty list.
#
# Input:
#   list_a: A list of stuff (your code shouldn't care what 'stuff' is)
#   list_b: Another list of stuff
#
# Output:
#   A list containing the zipped elements from list_a and list_b.
#
# Example:
#   >>> zipper([1, 2, 3], [4, 5, 6])
#   [(1, 4), (2, 5), (3, 6)]
def zipper(list_a, list_b):
    pass


# Only small deviations!
# 
# Let the deviation between two numbers be defined as the difference
# of their squares.
# 
# For example, the deviation between -3 and 7 is
# 
# |(-3)^2 - 7^2| = |9 - 49| = |-40| = 40
# 
# Given two lists, list_a and list_b, return a list of all the
# elements of list_a whose deviation from the corresponding
# element (i.e., the item with the same index) in list_b
# is less than 50. You *must* use the zipper function that
# you just defined.
#
# Input:
#   list_a: A list of integers
#   list_b: Another list of integers
#
# Output:
#   Return the elements of list_a that have a deviation of less
#   than 50 from their corresponding item in list_b. If the two
#   lists have different lengths, return an empty list.
#
# Example:
#   >>> only_small_deviations([1, 3, 0, 10], [2, 8, -1, 7])
#   [1, 0]
#
#   >>> only_small_deviations([1, 2], [1])
#   []
def only_small_deviations(list_a, list_b):
    pass


if __name__ == "__main__":
    def check(output, expected):
        if output != expected:
            return "FAILED!"
        else:
            return "PASSED!"

    print "zipper([1, 2, 3], [4, 5, 6]): " + check(
        zipper([1, 2, 3], [4, 5, 6]),
        [(1, 4), (2, 5), (3, 6)]
    )

    print "only_small_deviations([1, 3, 0, 10], [2, 8, -1, 7]): " + check(
        only_small_deviations([1, 3, 0, 10], [2, 8, -1, 7]),
        [1, 0]
    )
