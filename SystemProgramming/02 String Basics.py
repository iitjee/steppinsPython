>>> mystr = 'xxxSPAMxxx'
>>> mystr.find('SPAM')   #3
>>> mystr = 'xxaaxxaa'
>>> mystr.replace('aa', 'SPAM') 'xxSPAMxxSPAM


The find call returns the offset of the first occurrence of a substring, and replace does global search and replacement. Like 
all string operations, replace returns a new string instead of changing its subject in-place (recall that strings are 
immutable). 


In more recent Pythons, the in membership operator can often be used as an alternative to find if all we need is a yes/no answer (it tests for a substring’s presence).
    >>> mystr = 'xxxSPAMxxx'
    >>> 'SPAM' in mystr # substring search/test
    
   
   
    >>> mystr = '\t Ni\n' 
    >>> mystr.strip()   # strips whitespaces on either side
    'Ni'
    >>> mystr.rstrip()  #strips only on right side
    '\t Ni'
    
    
    
    
    >>> mystr = 'SHRUBBERY' >>> mystr.lower() 'shrubbery'
    >>> mystr.isalpha() True
    >>> mystr.isdigit() False
    >>> import string
    >>> string.ascii_lowercase 'abcdefghijklmnopqrstuvwxyz'
    >>> string.whitespace ' \t\n\r\x0b\x0c'
    
    
    
    
    >>> mystr = 'aaa,bbb,ccc'
    >>> mystr.split(',')        # split into substrings list
    ['aaa', 'bbb', 'ccc']
    
    >>> mystr = 'a b\nc\nd'
    >>> mystr.split()           # default delimiter: whitespace
    ['a', 'b', 'c', 'd']
    
    >>> delim = 'NI'
    >>> delim.join(['aaa', 'bbb', 'ccc'])     # join substrings list
    'aaaNIbbbNIccc'
    
    >>> ' '.join(['A', 'dead', 'parrot'])      # add a space between
    'A dead parrot'

    >>> chars = list('Lorreta')       # convert to characters list
    >>> chars
    ['L', 'o', 'r', 'r', 'e', 't', 'a']   
    
    >>> chars.append('!')
    >>> ''.join(chars)          # to string: empty delimiter
    'Lorreta!'
    
    
    split() is similar to splitlines() except that you will have '' i.e newline at the end in split() whereas that is removed in splitlines()
    
    
    
    
    These calls turn out to be surprisingly powerful.
 In fact, we can emulate the replace call we saw earlier in this section with a split/join combination:
      >>> mystr = 'xxaaxxaa'
      >>> 'SPAM'.join(mystr.split('aa'))       # str.replace, the hard way! 
      'xxSPAMxxSPAM'
      




For future reference, also keep in mind that Python doesn’t automatically convert strings to numbers, or vice versa; 
          >>> int("42"), eval("42")                # string to int conversions
          (42, 42)
          
          >>> str(42), repr(42)                   # int to string conversions
          ('42', '42')
          
          >>> ("%d" % 42), '{:d}'.format(42) 
          ('42', '42')
          
          >>> "42" + str(1), int("42") + 1         # via formatting expression, method # concatenation, addition
          ('421', 43)

 Python doesn’t assume you meant one or the other and convert automati- cally; as a rule of thumb, Python tries to avoid 
 agic—and the temptation to guess— whenever possible. 
 
 
 
 
 
 Other String Concepts in Python 3.X: Unicode and bytes:
 Technically speaking, the Python 3.X string story is a bit richer than I’ve implied here.
 Really, though, 3.X has two additional string types that support most str string oper- ations: bytes—a sequence of short integers for representing 8-bit binary data, and bytearray—a mutable variant of bytes.
 
 files in 3.X follow a similar dichotomy, using str in text mode  and bytes in binary mode. we’ll also see the same distinction for tools like sockets, which deal in byte strings today.
 
 
          ('42', '42')
