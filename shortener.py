import random
import string
import doctest
from urlparse import urlparse

# TODO
# use pickle or SQL to make data persistent
# add stats for numbers of click...
# http://gist.io/7268187

LETTERS_NUMBERS = ''.join((string.ascii_letters, string.digits))
CONVERT_LIST = list(LETTERS_NUMBERS)
URL_DICT = {}

def shortener(full_url):
    if not urlparse(full_url).scheme:
        full_url = ''.join(('http://', full_url))
    while True:
        # This is a way to have no predicatable short codes
        key = random.randint(0, 10 *(len(URL_DICT) + 100))
        if key not in URL_DICT:
            URL_DICT[key] = full_url
            break
    short_code = sixtytwo_to_str(ten_to_sixtytwo(key))
    return short_code


def ten_to_sixtytwo(number):
    """
    >>> ten_to_sixtytwo(0)
    [0]

    >>> ten_to_sixtytwo(62)
    [1, 0]

    >>> ten_to_sixtytwo(125)
    [2, 1]

    Base62 numbers are passed as lists
    """
    digits = []
    while True:
        quotient = number // 62
        remainder = number % 62
        digits.append(remainder)
        if quotient == 0:
            break
        number = quotient
    digits.reverse()
    return digits

def short_to_url(short_code):
    sixtytwo_key = str_to_sixtytwo(short_code)
    ten_key = sixtytwo_to_ten(sixtytwo_key)
    return URL_DICT[ten_key]


def sixtytwo_to_ten(number):
    """
    >>> sixtytwo_to_ten([0])
    0

    >>> sixtytwo_to_ten([2, 1])
    125

    Base62 numbers are passed as lists
    """
    n = len(number) - 1
    base_ten = 0
    for i, d in enumerate(number):
        base_ten += d * 62**(n - i)
    return base_ten

def str_to_sixtytwo(a_string):
    digits = [CONVERT_LIST.index(c) for c in a_string]
    return digits

def sixtytwo_to_str(number):
    """
    >>> sixtytwo_to_str([2, 1])
    'cb'

    >>> sixtytwo_to_str([0])
    'a'

    Base62 numbers are passed as a list
    """
    str_rep = [CONVERT_LIST[int(c)] for c in number]
    str_rep = ''.join(str_rep)
    return str_rep

if __name__ == '__main__':
    doctest.testmod()

