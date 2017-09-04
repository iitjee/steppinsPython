 sys and os modules form the core of much of Python’s system-related tool set
 
 
>>> import sys
>>> sys.platform, sys.maxsize, sys.version
          ('win32', 2147483647, '3.1.1 (r311:74483, Aug 17 2009, 17:02:12) ...more deleted...')
>>> if sys.platform[:3] == 'win': print('hello windows') ...
          hello windows
          
          
If you have code that must act differently on different machines, simply test the sys.platform string as done here; although 
most of Python is cross-platform, nonport- able tools are usually wrapped in if tests like the one here.




The Module Search Path:
sys.path is a list of directory name strings representing the true search path in a running Python interpreter. Because of 
that, this is the place to look to verify that your search path is really set as intended.‡
          >>> sys.path
          
          
The sys.path list is simply initialized from your PYTHONPATH setting—the content of any .pth path files located in Python’s 
directories on your machine plus system defaults—when the interpreter is first started up.
      >>> sys.path.append(r'C:\mydir')
      >>> sys.path
      ['', 'C:\\PP4thEd\\Examples', ...more deleted..., 'C:\\mydir'] //note that last item.
      
      
      Changes to sys.path are retained only until the Python process ends, and they must be remade every time you start a 
new Python program or session. However, some types of programs (e.g., scripts that run on a web server) may not be able to 
depend on PYTHONPATH settings; such scripts can instead configure sys.path on startup to include all the directories from 
which they will need to import modules. 

NOTE:
Notice the use of a raw string literal in the sys.path configuration code: because back- slashes normally introduce escape 
code sequences in Python strings, Windows users should be sure to either double up on backslashes when using them in DOS 
directory path strings (e.g., in "C:\\dir", \\ is an escape sequence that really means \), or use raw string constants to 
retain backslashes literally (e.g., r"C:\dir").If you inspect directory paths on Windows (as in the sys.path interaction 
listing), Python prints double \\ to mean a single \. 

Also note that most Python library calls accept either forward (/) or backward (\) slashes as directory path separators, 
regardless of the underlying platform. That is, / usually works on Windows too and aids in making scripts portable to Unix. 
Tools in the os and os.path modules, described later in this chapter, further aid in script path portability.




The Loadable Modules Table:
The sys module also contains hooks into the interpreter.
            >>> sys.modules
            >>> list(sys.modules.keys())
            
            
            >>> sys 
            >>> sys.modules['sys']
            
            >>> sys.getrefcount(myModule)       #an object’s reference count
            >>> sys.builtin_module_names        #names of modules built-in to the Python executable
            
            
these are mostly Python internals information, but such hooks can sometimes become important to programmers writing tools 
for other programmers to use.







Exception Details:
Other attributes in the sys module allow us to fetch all the information related to the most recently raised Python 
exception. 
          >>> try:
          ...     raise IndexError
          ... except:
          ...     print(sys.exc_info())
          ... 
          


Other Modules:
• Command-line arguments show up as a list of strings called sys.argv.
• Standard streams are available as sys.stdin, sys.stdout, and sys.stderr.
• Program exit can be forced with sys.exit calls.
Since these lead us to bigger topics, though, we will cover them in sections of their own.
