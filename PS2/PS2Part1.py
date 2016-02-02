# CS196 homework problem set 2, file 1/4
#
# Welcome to week 2! The problems this week have gotten much tougher, but
# so have you! Can you solve them all?


# I can haz vowels?
#
# Input:
#   word: a string
#
# Output:
#   Return True if the input string contains any vowels (either uppercase
#   or lowercase). Return False if it does not. Do not print anything.
#   Vowels for the sake of this problem are 'a', 'e', 'i', 'o', and 'u'.
#
# Example:
#   >>> check_vowels('htgj')
#   False
#
#   >>> check_vowels('abc')
#   True
#
#   >>> check_vowels('ABC')
#   True
def check_vowels(word):
    pass


# Snow Day
#
# Input:
#   snow: the inches of snow on the ground (a float)
#   temp: the current temperature (a float)
#   classes_canceled: True if classes are canceled, False otherwise
#
# Output:
#   If there is 6 or more inches of snow AND classes are canceled, return "snowman".
#   Otherwise, if the temperature is between 0 and 32 (inclusive) OR there is
#   less than 6 inches of snow, return "snowball fight".
#   In all other cases, return "netflix".
#
# Example:
#   >>> snow_day(2.0, 10.0, False)
#   'snowball fight'
#
#   >>> snow_day(7.0, 25.0, True)
#   'snowman'
#
#   >>> snow_day(9.0, 45.0, True)
#   'netflix'
def snow_day(snow, temp, classes_canceled):
    pass


# String Repeater
# A "very very very very very" useful function
#
# Input:
#   template: a string
#   n: a positive integer
#
# Output:
#   Return a single string that is the value of `template` repeated `n` times.
#   Do not add any additional characters (no added spaces). Do not print anything.
#
# Example:
#   >>> string_repeater("hello!", 3)
#   'hello!hello!hello!'
#
#   >>> string_repeater("very", 5)
#   'veryveryveryveryvery'
def string_repeater(template, n):
    pass


# Lowest Common Multiple
#
# Input:
#   a: a positive integer
#   b: a positive integer
#
# Output:
#   Return the smallest positive integer that is divisible by
#   both a and b. Do not print anything.
#
# Hint:
#   Use the modulo operator (a % b) to check divisibility.
#
# Example:
#   >>> lowest_common_multiple(3, 5)
#   15
#
#   >>> lowest_common_multiple(12, 80)
#   240
def lowest_common_multiple(a, b):
    pass


# Reverse
#
# Input:
#    s: a string
#
# Output:
#    Return the reverse of the string `s`. Do not print anything.
#
# Example:
#   >>> reverse("Hello World!")
#   '!dlroW olleH'
#
#   >>> reverse("car")
#   'rac'
def reverse(s):
    pass


# ShortLongShort
#
# Input:
#   a: a string
#   b: a string
#
# Output:
#   If a is shorter than or the same length as b, return the value of a + b + a.
#   Otherwise, return the value of b + a + b. Do not print anything.
#
# Example:
#   >>> shortlongshort("car", "horn")
#   'carhorncar'
#
#   >>> shortlongshort("horse", "car")
#   'carhorsecar'
#
#   >>> shortlongshort("aa", "bb")
#   'aabbaa'
def shortlongshort(a, b):
    pass


# Substring
#
# Input:
#   s: a string
#   i: the inclusive starting index (an int)
#   j: the exclusive ending index (an int)
#
# Output:
#   Return a string containing the ith to the (j-1)th characters of the input string.
#   If i is greater than or equal to j, return an empty string ("").
#   If i or j-1 is not a valid index in the input string, return an empty string ("").
#
# Example:
#   >>> substring("Hello", 1, 3)
#   'el'
#
#   >>> substring("Pineapple", 0, 4)
#   'Pine'
#
#   >>> substring("Corn", 1, 5)
#   ''
#
#   >>> substring("Corn", 3, 2)
#   ''
#
#   >>> substring("Corn", 2, 4)
#   'rn'
def substring(s, i, j):
    pass


# Prefix appender (u wot m8?)
#
# Input:
#   s: a string
#   n: the number of characters to modify (an int)
#
# Output:
#   Return the value of the input string, with the first `n` characters
#   removed from the beginning and appended to the end. If `n` is equal
#   to the length of the string, just return the string itself. If `n`
#   is greater than the length of the string, return an empty string ("").
#
# Hint:
#   Use the substring function you just defined! While you're at it,
#   can you see why the upper bound of the substring is exclusive
#   rather than inclusive? ;-)
#
# Example:
#   >>> append_prefix("CompSci", 4)
#   'SciComp'
#
#   >>> append_prefix("oxygen", 9001)
#   ''
def append_prefix(s, n):
    pass


if __name__ == "__main__":
    def check(output, expected):
        if output != expected:
            return "FAILED!"
        else:
            return "PASSED!"

    print "check_vowels('banana'): " + check(check_vowels('banana'), True)
    print "string_repeater('b', 5): " + check(string_repeater('b', 5), 'bbbbb')
    print "string_repeater('doot ', 2): " + check(string_repeater('doot ', 2), 'doot doot ')
    print "lowest_common_multiple(3, 5): " + check(lowest_common_multiple(3, 5), 15)
    print "lowest_common_multiple(9, 3): " + check(lowest_common_multiple(9, 3), 9)
    print "snow_day(6.0, 32.0, False): " + check(snow_day(6.0, 32.0, False), 'snowball fight')
    print "snow_day(8.0, 20.0, True): " + check(snow_day(8.0, 20.0, True), 'snowman')
    print "reverse('Hello World!'): " + check(reverse("Hello World!"), '!dlroW olleH')
    print "shortlongshort('small', 'bigger'): " + check(shortlongshort("small", "bigger"), 'smallbiggersmall')
    print "substring('bobby', 0, 3): " + check(substring('bobby', 0, 3), 'bob')
    print "append_prefix('CompSci', 4): " + check(append_prefix('CompSci', 4), 'SciComp')
