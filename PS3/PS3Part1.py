# CS196 homework problem set 3, file 1/5
#
# Welcome to week 3! Once again, the problems have gotten harder, so be prepared!
# We've laid traps in many of the problems this week, so make sure to check your
# corners (or rather, corner cases)!


# Modify the value!
#
# This method is trying to change the value in one position of the tuple but
# it seems like Python is giving us an error when we try to do that. Why is
# that? Can you change the data structure used in this problem to another one
# so that it supports changing the values of items in it?
#
# Input:
#   values: A tuple with at least one element
#
# Output:
#   Return a tuple with the same elements as the input,
#   but with the first value replaced by 0.
#
# Example:
#   >>> modify_value((5, 3, 4, 2, 6))
#   (0, 3, 4, 2, 6)
def modify_value(values):
    values[0] = 0
    return values


# Triple Expression
#
# Given a 3-tuple, return the first element minus the second plus the third.
# You must use tuple unpacking - no points will be given for a solution that
# accesses items by using an index (i.e. t[0], t[1], etc.)
#
# Input:
#   t: a tuple with 3 integers
#
# Output:
#   Return the first value - the second value + the third value.
#
# Example:
#   >>> triple_expression((1, 5, 3))
#   -1
def triple_expression(t):
    pass


# Longer than five
#
# This method counts the number of strings in the input list that
# have a length greater than five.
#
# Input:
#   values: A list of strings with varying lengths
#
# Output:
#   Return the number of strings in the list with lengths greater than 5.
#
# Example:
#   >>> longer_than_five(['hello', 'ayy', 'this is longer', 'wow', 'this is also pretty long'])
#   2
def longer_than_five(values):
    pass


# Gimmie the end!
#
# This method gives you the last n elements of the tuple given!
#
# Input:
#   values: a tuple of integers
#   n - the number of items to return from the end of the tuple
#
# Output:
#   Return a tuple containing the last n elements of the input.
#
# Note:
#   n will always be >= 0, and never larger than the length of the tuple.
#
# Example:
#   >>> gimmie_the_end((2, 4, 5, 6, 6, 7), 3)
#   (6, 6, 7)
def gimmie_the_end(values, n):
    pass


# What a funny accent!
# 
# Replace any vowels (a, e, i, o, u) in a string with the letter e.
# Don't use the replace() method; instead, use something with lists.
#
# Input: 
#   phrase: a string (all letters will be lowercase)
#
# Output:
#   Return the input string, with all vowels changed to 'e'.
#
# Example:
#   >>> accentify("accentify")
#   "eccentefy"
def accentify(phrase):
    pass


# Don't cross me.
#
# Given two triples (tuples of three elements), find their cross product.
# For the majority of you who haven't seen what a cross product is:
# https://www.mathsisfun.com/algebra/vectors-cross-product.html
# Look at the second method of calculating the cross product.
# 
# Input:
#   first: a triple of numbers
#   second: another triple of numbers
#
# Output:
#   Return a triple representing the cross product
#
# Example:
#   >>> cross_product((2, 3, 4), (5, 6, 7))
#   (-3, 6, -3)
def cross_product(first, second):
    pass


if __name__ == "__main__":
    def check(output, expected):
        if output != expected:
            return "FAILED!"
        else:
            return "PASSED!"

    print "cross_product((2, 3, 4), (5, 6, 7)): " + check(cross_product((2, 3, 4), (5, 6, 7)), (-3, 6, -3))
    print "accentify(\"accentify\"): " + check(accentify("accentify"), "eccentefy")
    print "modify_value((2, 3, 4)): " + check(modify_value((2, 3, 4)), (0, 3, 4))
    print "triple_expression((1, 5, 3)): " + check(triple_expression((1, 5, 3)), -1)
    print "longer_than_five(['this is longer', 'wow']): " + check(longer_than_five(['this is longer', 'wow']), 1)
    print "gimmie_the_end((2, 4, 5, 6, 6, 7), 3): " + check(gimmie_the_end((2, 4, 5, 6, 6, 7), 3), (6, 6, 7))
