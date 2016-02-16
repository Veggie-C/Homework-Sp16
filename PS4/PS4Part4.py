# CS196 homework problem set 4, file 4/4
#
# CS196 Translate (TM)
#
# Ever wanted to learn how (not) to speak a new language? Now you
# can, thanks to our awesome(ish) language translation dictionary!
#
# Input:
#   translation_map: a dict mapping *LOWERCASE* words from the input to the output language
#   text: a string to translate (containing alphabetical letters and spaces only)
#
# Output:
#   Return the input text, with all words (sequences of letters separated by spaces)
#   converted to the output language by looking up the original word in
#   `translation_map`.
#
#   If the translation dict does not contain the original word, use the original
#   word. If the first character of the original word was capitalized, capitalize the
#   first character of the output. You do not need to handle special cases
#   such as plurals, a/an, contractions, all-caps words, etc.
#
# Hint:
#   These string methods may be useful to you:
#      lower(), upper(), islower(), isupper(), split(), join()
#
# Example:
#   # Wapanese
#   >>> translate_text({"i": "watashi", "like": "suki", "dogs": "inu"}, "I like dogs")
#   'Watashi suki inu'
#
#   # Chinglish
#   >>> translate_text({"you": "ni", "lost": "shule", "the": "gai", "game": "youxi"}, "You lost The Game")
#   'Ni shule Gai Youxi'
#
#   # 13375p34k
#   >>> translate_text({"noob": "n00b", "elite": "1337", "hacker": "haxx0r"}, "I am elite hacker")
#   'I am 1337 haxx0r'
def translate_text(translation_map, text):
    pass


if __name__ == "__main__":
    def check(output, expected):
        if output != expected:
            return "FAILED!"
        else:
            return "PASSED!"

    print 'translate_text({"i": "watashi", "like": "suki", "dogs": "inu"}, "I like dogs"): ' + check(
        translate_text({"i": "watashi", "like": "suki", "dogs": "inu"}, "I like dogs"),
        'Watashi suki inu')

    print 'translate_text({"you": "ni", "lost": "shule", "the": "gai", "game": "youxi"}, "You lost The Game"): ' + check(
        translate_text({"you": "ni", "lost": "shule", "the": "gai", "game": "youxi"}, "You lost The Game"),
        'Ni shule Gai Youxi')

    print 'translate_text({"noob": "n00b", "elite": "1337", "hacker": "haxx0r"}, "I am elite hacker"): ' + check(
        translate_text({"noob": "n00b", "elite": "1337", "hacker": "haxx0r"}, "I am elite hacker"),
        'I am 1337 haxx0r')
