# CS196 homework problem set 4, file 2/4
#
# Cycle length
#
# Let's play a game! We have a bunch of tiles, and each
# tile specifies the tile you must jump to next. You start
# on tile 0, and your goal is to jump between tiles to return
# to tile 0.
#
# Input:
#   x: a dict mapping the # of each tile to the # of the next tile
#
# Output:
#   Return the number of "hops" needed for you to return to tile 0.
#   If you are caught in an infinite loop (no way for you to return to
#   tile 0), return -1.
#
# Example:
#   >>> cycle_length({0:1, 1:5, 2:3, 3:0, 4:1, 5:2})
#   5
#
#   >>> cycle_length({0:1, 1:2, 2:1})
#   -1
#
#   >>> cycle_length({0:0})
#   1
def cycle_length(x):
    pass


if __name__ == "__main__":
    def check(output, expected):
        if output != expected:
            return "FAILED!"
        else:
            return "PASSED!"

    print "cycle_length({0:1, 1:5, 2:3, 3:0, 4:1, 5:2}): " + check(
        cycle_length({0:1, 1:5, 2:3, 3:0, 4:1, 5:2}), 5)

    print "cycle_length({0:1, 1:2, 2:1}): " + check(
        cycle_length({0:1, 1:2, 2:1}), -1)

    print "cycle_length({0:0}): " + check(
        cycle_length({0:0}), 1)
