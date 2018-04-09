# safe_str()

say GOOD-BYE to UnicodeEncodeError: 'ascii' codec can't encode character in position : ordinal not in range(128)
  - Work for both python 2 and 3
  - STOP using str() and sys.setdefaultencoding('UTF8')

# Demo
  - Before:
```
print 'café'.decode('utf-8') # any text cause you an UnicodeEncodeError
>>> UnicodeEncodeError: 'ascii' codec can't encode character u'\xe9' in position 3: ordinal not in range(128)
```

 - After:
```
print safe_str('café'.decode('utf-8'))
>>> café
```

# Usage
copy this snippet to your code:
```python
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
```


