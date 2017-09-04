A Python file can be used in either of two ways—as a script or as a library.


(more.py)
        def more(text, numlines=15): 
          lines = text.splitlines()   # like split('\n') but no '' at end
          while lines:
            chunk = lines[:numlines]
            lines = lines[numlines:]
            for line in chunk: print(line)
            if lines and input('More?') not in ['y', 'Y']: break   #want more lines prompt

        if __name__ == '__main__':
          import sys                                 # when run, not imported 
          more(open(sys.argv[1]).read(), 10)         # page contents of file on cmdline


Recall that every Python module has a built-in __name__ variable that Python sets to the __main__ string only when the file is 
run as a program, not when it’s imported as a library.

 when this script is run as a top-level program, the more function in this file is executed automatically by the last line in 
 the file.
 This simple trick turns out to be one key to writing reusable script code: by coding program logic as functions rather than a
 s top-level code, you can also import and reuse it in other scripts i.e 
             we can run more.py by itself or
             import and call its 'more' function elsewhere. 

>>> from more import more
>>> import sys
>>> more(sys.__doc__)


