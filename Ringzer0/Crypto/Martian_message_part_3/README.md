# Martian message part 3

__PROBLEM__

RU9CRC43aWdxNDsxaWtiNTFpYk9PMDs6NDFS

__SOLUTION__

So the given string is base64 encoded. If you'll decode the string you'll get something like `'EOBD.7igq4;1ikb51ibOO0;:41R'`. Now this is not the correct flag. Since I have done some cryptopals I realized that it might be a single byte XOR so. I wrote a small piece of code.

```python
def xor(s1, s2):
    """Find Xor between two strings with bytes
    """
    output = b''
    for char in s1:
        output += bytes([char^s2])

    return output

>>> for i in range(256):
  2    if b'FLAG' in xor(msg,i):
  3        print(xor(msg,i))
b'FLAG-4jdr782jha62jaLL38972Q'
```

And boom we have it.

FLAG - `FLAG-4jdr782jha62jaLL38972Q`
