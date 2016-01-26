# CS196 homework problem set 1, file 1/3
#
# Most of these problems can be solved in a single line of code.
# Make sure to do *exactly* what the specifications tell you to!
# Also don't assume too much (if we said x is a number, don't assume
# you're only dealing with integers!)
#
# If the specification tells you to *print* a value, do it using:
#     print 'This is the output!'
# If the specification tells you to *return* a value, you should use:
#     return 'This is the output!'
# Do not confuse the two, or you will not receive credit for that problem!


# Hello, world!
#
# Input: None.
#
# Output:
#   Print exactly "Hello, world!" to the console. Do not return anything.
def hello_world():
    pass


# Identity
# 
# Input:
#   x - something (or more specifically, anything)
#
# Output:
#   Return x (the input). Do not print anything. In fact, we pretty much
#   just gave you the answer.
def identity(x):
    pass


# Increment
#
# Input:
#   x - an integer
#
# Output:
#   Return the value of x+1. Do not print anything.
def increment(x):
    pass


# Can you repeat that?
# 
# Input:
#   x - a string
# 
# Output:
#   Print the value of x twice, *on a single line*! Do not return anything.
#   For example, if x is "hi", your code should print "hihi".
def repeat_that(x):
    pass


# Can you repeat that, again?
#
# Input:
#   x - a string
#
# Output:
#   Call the function you just defined, repeat_that, twice. The value of 
#   x should be printed 4 times, 2 times on each line.
def repeat_that_again(x):
    pass


# Order of operations
# This code is broken. Fix it so that it returns 15. *You may not delete
# any characters*!
#
# Input: None.
# 
# Output:
#   Return the integer 15. Do not print anything.
def give_me_15():
    return 2 + 3 * 3


# Is it even?
# Check whether the input value is an even integer.
# 
# Input: 
#   x - the number to check (an integer)
# 
# Output:
#   Return True if x is even, and False if x is odd. Do not print anything.
def is_it_even(x):
    pass


# Y U NO DECIMAL?!
# Something is horribly wrong. The code below should return 4.5, but
# for some reason it's off by 0.5! Fix the code, but *do not delete 
# any characters*.
#
# Input: None.
#
# Output:
#   Return 4.5. Do not print anything.
def y_u_no_decimal():
    return 9 / 2


# Pythagorean theorem
# Calculate the length of the hypotenuse of a right triangle
# given the lengths of the legs, a and b.
# 
# Input:
#   a - the length of the first leg (a number greater than 0)
#   b - the length of the second leg (a number greater than 0)
#
# Output:
#   Return the numeric value of the hypotenuse. Do not print anything.
def pythagorean(a, b):
    pass

# Below are some test cases that we have written up for you!
# Feel free to add more to test your code! Though be warned, 
# our grading program will test more cases than this... so make
# sure your functions are correct!

# If you want to learn about this __name__ == "__main__",
# see http://stackoverflow.com/questions/419163/what-does-if-name-main-do
if __name__ == "__main__":
    print "Running hello_world():"
    hello_world()
    print "Running repeat_that(\"double\")"
    repeat_that("double")
    print "Running repeat_that_again(\"me\")"
    repeat_that_again("me")

    print "identity(3) == " + str(identity(3))
    print "identity('bob') == " + identity('bob')
    print "increment(195) == " + str(increment(195))
    print "is_it_even(4) == " + str(is_it_even(4))
    print "pythagorean(3, 4) == " + str(pythagorean(3, 4))
