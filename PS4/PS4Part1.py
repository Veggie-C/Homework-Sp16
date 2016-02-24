# CS196 homework problem set 4, file 1/4
#
# Yo dawg, I heard you like lists so we put some lists in yo
# lists so you can loop while you loop. Oh yeah, and we have
# some dictionaries. Well guess what? We put some lists
# in those too.

# List flattener
#
# Input:
#   x: a 2D list of things (who knows what?)
#
# Output:
#   Return a 1D list containing the elements from each of
#   the inner lists from the input, in the same order that
#   they originally appeared in each inner list.
#
# Example:
#   >>> flatten_list([[1, 2.5, 3], [4, 5], [], ["BOB"]])
#   [1, 2.5, 3, 4, 5, "BOB"]
def flatten_list(x):
    pass


# It's as easy as ABC
#
# Input:
#   x: a dict mapping letters to the number of that letter in your soup
#
# Output:
#   Return a string containing the letters in your soup! The order of
#   the characters doesn't matter.
#
# Example:
#   >>> alphabet_soup({"A": 5, "B": 10})
#   "AAAAABBBBBBBBBB"
def alphabet_soup(x):
    pass


# Caching is the cause of, and solution to all problems in CS
#
# Input:
#   x: a list of strings with no duplicate entries
#
# Output:
#   Return a dict containing the items in x mapped to their 
#   index in x.
#
# Example:
#   >>> create_lookup(["apple", "banana", "cactus"])
#   {'apple': 0, 'banana': 1, 'cactus': 2}
def create_lookup(x):
    pass


# Item counter
#
# Input:
#   x: a list of strings
#
# Output:
#   Return a dict containing each value in x mapped to the
#   number of times it appears in x.
#
# Example:
#   >>> count_items(["apple", "banana", "cactus", "banana"])
#   {'apple': 1, 'banana': 2, 'cactus': 1}
def count_items(x):
    pass


# String decoder
#
# Input:
#   key: a dict containing a mapping from character to character
#   rounds: the number of times to decode a character (a positive int)
#   s: the string to decode
#
# Output:
#   Return the decoded string. The algorithm is as follows:
#   For each character in s, decode it by looking up the character
#   in the key, then taking the resulting character and looking it up
#   in the key again, repeating this process the specified number of 
#   rounds.
#
# Example:
#   >>> decode_string({'a':'b', 'b':'c', 'c':'a'}, 4, "abc")
#   'bca'
def decode_string(key, rounds, s):
    pass


# Longest strings
#
# Input:
#   data: a 2D list of strings with varying inner list lengths
# 
# Output:
#   Return a list containing the longest string from each
#   inner list. If two strings have equal length, use the
#   one the comes first. If an inner list is empty, ignore it.
#
# Example:
#    >>> longest_strings([["aaaa", "b"], ["cc", "dd", "ee"], []])
#    ["aaaa", "cc"]
def longest_strings(data):
    pass


# String categorizer
#
# Input:
#   data: a list of strings
#
# Output:
#   Return a dictionary with two keys: 'strange' and 'normal'. 'strange'
#   should map to a list of strings from the input that either have an
#   odd number of characters, or have no vowels (a, e, i, o, u and their
#   uppercase equivalents). 'normal' should map to a list containing
#   everything else.
#
# Example:
#   >>> string_categorizer(['apple', 'flying', 'BLAH'])
#   {'strange': ['apple'], 'normal': ['flying', 'BLAH']}
def string_categorizer(data):
    pass


# w00t linear algebra
# https://en.wikipedia.org/wiki/Identity_matrix
#
# Input:
#   n: the dimensions of the output matrix (a positive int)
#
# Output:
#   Return a n-by-n identity matrix. This should
#   be a 2D list in row-major order (i.e., x[0][1] should
#   give the item in row 0, column 1, although for this
#   problem it doesn't actually make a difference).
#
# Example:
#   >>> identity_matrix(3)
#   [[1, 0, 0], [0, 1, 0], [0, 0, 1]]
def identity_matrix(n):
    pass


# Cache ALL the things!
#
# Input:
#   n: the upper limit of your multiplication table (a positive int)
#
# Output:
#   Return a 2D list representing the multiplcation table
#   from 0 to n (inclusive). For all x, y between 0 and n,
#   the value at [x][y] should equal x * y.
#
# Example:
#    >>> multiplication_table(2)
#    [[0, 0, 0], [0, 1, 2], [0, 2, 4]]
def multiplication_table(n):
    pass


# Still better than DARS
#
# Input:
#   gpa_map: a dict mapping letter grades to GPA values
#   credit_map: a dict mapping course names to credit values
#   class_scores: a list containing tuples in the format (class, grade)
#
# Output:
#   Return the total GPA, calculated by the formula
#   <total weighted GPA>/<total credits>. The weighted GPA for each class is 
#   calculated by <GPA for that class> * <credits for that class>.
#   If the total credits equal zero, return zero.
#
# Example:
#   >>> calculate_gpa(
#   ...     {'A': 4.0, 'B': 3.7, 'C': 3.4},
#   ...     {"CS196": 1, "CS125": 4},
#   ...     [("CS196", 'A'), ("CS125", 'B')])
#   3.76
def calculate_gpa(gpa_map, credit_map, class_scores):
    pass


if __name__ == "__main__":
    def check(output, expected):
        if output != expected:
            return "FAILED!"
        else:
            return "PASSED!"

    print 'flatten_list([[1, 2.5, 3], [4, 5], [], ["BOB"]]): ' + check(
        flatten_list([[1, 2.5, 3], [4, 5], [], ["BOB"]]),
        [1, 2.5, 3, 4, 5, "BOB"])

    print "alphabet_soup({'A': 5, 'B': 10}): " + check(
        "".join(sorted(alphabet_soup({"A": 5, "B": 10}) or "")),
        "AAAAABBBBBBBBBB")

    print "create_lookup(['apple', 'banana', 'cactus']): " + check(
        create_lookup(["apple", "banana", "cactus"]),
        {'apple': 0, 'banana': 1, 'cactus': 2})

    print 'count_items(["apple", "banana", "cactus", "banana"]): ' + check(
        count_items(["apple", "banana", "cactus", "banana"]),
        {'apple': 1, 'banana': 2, 'cactus': 1})

    print "decode_string({'a':'b', 'b':'c', 'c':'a'}, 4, 'abc'): " + check(
        decode_string({'a':'b', 'b':'c', 'c':'a'}, 4, 'abc'),
        "bca")

    print 'longest_strings([["aaaa", "b"], ["cc", "dd", "e"], []]): ' + check(
        longest_strings([["aaaa", "b"], ["cc", "dd", "e"], []]),
        ["aaaa", "cc"])

    print "string_categorizer(['bob','camp','spring','valentine']): " + check(
        string_categorizer(['bob','camp','spring','valentine']),
        {'strange': ['bob', 'valentine'], 'normal': ['camp', 'spring']})

    print "identity_matrix(3): " + check(
        identity_matrix(3),
        [[1, 0, 0], [0, 1, 0], [0, 0, 1]])

    print "multiplication_table(3): " + check(
        multiplication_table(3),
        [[0, 0, 0, 0], [0, 1, 2, 3], [0, 2, 4, 6], [0, 3, 6, 9]])

    print "calculate_gpa(...): " + (abs(3.76 -
        (calculate_gpa(
            {'A': 4.0, 'B': 3.7, 'C': 3.4},
            {"CS196": 1, "CS125": 4},
            [("CS196", 'A'), ("CS125", 'B')]) or 0)
        ) < 0.001 and "PASSED!" or "FAILED!")
