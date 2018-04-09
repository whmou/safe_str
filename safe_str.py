#!/usr/bin/python
# -*- coding: utf-8 -*-
import sys


def safe_str(text):
    """
    helper function to print/write text safely,
    work for both python 2, 3.
    say good-bye to UnicodeEncodeError: 'ascii' codec can't encode
    character in position : ordinal not in range(128)
    :param text: take types (str, unicode, bytes, int, float, long, NoneType, Boolean)
    """
    if (sys.version_info[0] < 3 and isinstance(text, unicode)) or (
            sys.version_info[0] == 3 and isinstance(text, bytes)):
        text = text.encode('utf-8')
    return text


print (safe_str(u'\xea\x80\x80abcd\xde\xb4'))
print (type(safe_str('測試')))
print (safe_str('測試'))
print (type(safe_str(1)))
print (safe_str("test"))
print (safe_str(None))
print (safe_str(True))
