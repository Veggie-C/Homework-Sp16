# CS196 homework problem set 3, file 2/5
#
# Washing the Dishes
#
# In an egregious violation of instructor ethics, Mark has offered to give
# you 100% on this problem in return for washing his dishes. Well, not
# exactly washing his dishes - just replacing the water when it gets too
# dirty. The dirtiness of dishes is represented by a positive integer, and
# whenever the dish is washed, the water's dirtiness increases by that amount.
# 
# Your job is to log everything that happens - the dirtiness of the dishes,
# and the number of times you've changed the water. Your log should be a list
# of the dirtiness values of the dishes that you washed, in the order you 
# washed them.
# 
# After the water becomes too dirty (the total dirtiness is equal to or greater
# than the given threshold), add the string "CHANGE WATER" (all caps) to the list,
# and reset the water dirtiness to zero.
#
# Then, after you're done, make sure to drain the dirty water by
# adding "DRAIN WATER" at the end of your list!
# You should never change the water after all dishes have been washed -
# that is, you should not have "CHANGE WATER" immediately followed by
# "DRAIN WATER" - that would be a waste!
# 
# Finally, return your log, so we know whether you followed our instructions
# correctly.
#
# Input:
#   dishes: a list of positive integers representing the dirtiness of each dish
#   dirty_threshold: a positive integer; when this value is exceeded, change the water.
#
# Output:
#   Return the list of actions performed (see instructions above)
#
# Example:
#   >>> clean_my_dishes([3, 5, 2, 2], 7)
#   [3, 5, "CHANGE WATER", 2, 2, "DRAIN WATER"]
#
#   >>> clean_my_dishes([4, 6, 15, 1, 2, 1, 11], 10)
#   [4, 6, "CHANGE WATER", 15, "CHANGE WATER", 1, 2, 1, 11, "DRAIN WATER"]
#
#   >>> clean_my_dishes([8, 1, 7], 26)
#   [8, 1, 7, "DRAIN WATER"]
def clean_my_dishes(dishes, dirty_threshold):
    pass


if __name__ == "__main__":
    def check(output, expected):
        if output != expected:
            return "FAILED!"
        else:
            return "PASSED!"

    print "clean_my_dishes([3, 5, 2, 2], 7): " + check(
        clean_my_dishes([3, 5, 2, 2], 7),
        [3, 5, "CHANGE WATER", 2, 2, "DRAIN WATER"]
    )

    print "clean_my_dishes([4, 6, 15, 1, 2, 1, 11], 10): " + check(
        clean_my_dishes([4, 6, 15, 1, 2, 1, 11], 10),
        [4, 6, "CHANGE WATER", 15, "CHANGE WATER", 1, 2, 1, 11, "DRAIN WATER"]
    )

    print "clean_my_dishes([8, 1, 7], 26): " + check(
        clean_my_dishes([8, 1, 7], 26),
        [8, 1, 7, "DRAIN WATER"]
    )
