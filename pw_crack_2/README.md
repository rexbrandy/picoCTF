Python 3.11.6 (main, Nov  2 2023, 04:51:19) [Clang 14.0.0 (clang-1400.0.29.202)] on darwin
Type "help", "copyright", "credits" or "license" for more information.
>>> chr(0x33)
'3'
>>> print(chr(0x33), chr(0x39, chr(0x63), chr(0x65))
... 
... 
... ;
  File "<stdin>", line 4
    ;
    ^
SyntaxError: invalid syntax
>>> print(chr(0x33), chr(0x39), chr(0x63), chr(0x65))
3 9 c e
>>> 

