os is the larger of the two core system modules.
contains all of the usual operating-system calls you use in C programs and shell scripts

Technically, this module provides POSIX tools—a portable standard for operating-system calls—along with platform- independent 
directory processing tools as the nested module os.path.

Scripts written with os and os.path can usually be run unchanged on any platform


![summary](https://user-images.githubusercontent.com/20602254/30064179-99d9b1d2-926e-11e7-99f8-3aa3783e7fa6.png)



>>>import os
>>> dir(os)       #list of all attributes

>>> dir(os.path)    #besides os, os.opath module exports even more tools, most of which are related to processing file and 
                      directory names 


Administrative Tools:
      >>> os.getpid()         #gives the calling process’s process ID
      >>> os.getcwd()         #current working directory

      >>> os.chdir(r'C:\Users')   #change dir (important)
      >>> os.getcwd()


Portability Constants:
      os.pathsep,     #character that sep- arates directories on directory lists, : for POSIX and ; for DOS and Windows
      os.sep,         #character used to separate directory components on your platform (\ on Windows, / for POSIX machines, 
                      and : on some Macs)
      os.pardir, 
      os.curdir, 
      os.linesep
By using such attributes when composing and decomposing system-related strings in our scripts, we make the scripts fully 
portable. For instance, a call of the form dir path.split(os.sep) will correctly split platform-specific directory names 
into compo- nents, though dirpath may look like dir\dir on Windows, dir/dir on Linux, and dir:dir on some Macs. 



Common os.path Tools:
The nested module os.path provides a large set of directory-related tools of its own.
      checking a file’s type (isdir, isfile, and others); 
      testing file existence (exists); and 
      fetching the size of a file by name (getsize):
      splitting and joining directory path strings (split, join, basename, dirname, splittext)

      
      >>> os.path.isdir(r'C:\Users'), os.path.isfile(r'C:\Users')                 #t, f
      >>> os.path.isdir(r'C:\config.sys'), os.path.isfile(r'C:\config.sys')       #f, t
      >>> os.path.isdir('nonesuch'), os.path.isfile('nonesuch')                   #f, f
      >>> os.path.exists(r'c:\Users\Brian')                       #f
      >>> os.path.exists(r'c:\Users\Default')                     #t
      >>> os.path.getsize(r'C:\autoexec.bat')                     #24
      
      
      >>> os.path.split(r'C:\temp\data.txt')                          #('C:\\temp', 'data.txt')
      >>> os.path.join(r'C:\temp', 'output.txt')                      #'C:\\temp\\output.txt'
      
      >>> name = r'C:\temp\data.txt'
      >>> os.path.dirname(name), os.path.basename(name)               #('C:\\temp', 'data.txt')
      
      >>> name = '/home/lutz/temp/data.txt'
      >>> os.path.dirname(name), os.path.basename(name)               #('/home/lutz/temp', 'data.txt')
      
      >>> os.path.splitext(r'C:\PP4thEd\Examples\PP4E\PyDemos.pyw')   #('C:\\PP4thEd\\Examples\\PP4E\\PyDemos', '.pyw')



 it’s almost equivalent to use string split and join method calls with the portable os.sep string, but not exactly:
      >>> os.sep                                                     #'\\'
      >>> pathname = r'C:\PP4thEd\Examples\PP4E\PyDemos.pyw'
      
      >>> os.path.split(pathname)                                   #('C:\\PP4thEd\\Examples\\PP4E', 'PyDemos.pyw')
      >>> pathname.split(os.sep)                              # ['C:', 'PP4thEd', 'Examples', 'PP4E', 'PyDemos.pyw']
      
      >>> os.sep.join(pathname.split(os.sep))                   #'C:\\PP4thEd\\Examples\\PP4E\\PyDemos.pyw'
      >>> os.path.join(*pathname.split(os.sep))                 #'C:PP4thEd\\Examples\\PP4E\\PyDemos.pyw'

The last join call require individual arguments (hence the *) but doesn’t insert a first slash because of the Windows drive 
syntax; use the preceding str.join method instead if the difference matters.


normpath call comes in handy if your paths become a jumble of Unix and Windows separators:
            >>> mixed                                                   #'C:\\temp\\public/files/index.html'
            >>> os.path.normpath(mixed)                                 #'C:\\temp\\public\\files\\index.html'
            >>> print(os.path.normpath(r'C:\temp\\sub\.\file.ext'))     #C:\temp\sub\file.ext
           
            
abspath portably returns the full directory pathname of a file; it accounts for adding the current directory as a path prefix, .. parent syntax, and more:
          >>> os.getcwd()                                         'C:\\Users'
          >>> os.path.abspath('')                                 'C:\\Users'
       
          >>> os.path.abspath('temp')                             'C:\\Users\\temp'
          >>> os.path.abspath(r'PP4E\dev')                        'C:\\Users\\PP4E\\dev'
          
          >>> os.path.abspath('.')                                'C:\\Users'
          >>> os.path.abspath('..')                               'C:\\'
          >>> os.path.abspath(r'..\examples')                     'C:\\examples'
          
          >>> os.path.abspath(r'C:\PP4thEd\chapters')             'C:\\PP4thEd\\chapters'
          >>> os.path.abspath(r'C:\temp\spam.txt')                'C:\\temp\\spam.txt'
          
Because filenames are relative to the current working directory when they aren’t fully specified paths, the os.path.abspath 
function helps if you want to show users what directory is truly being used to store a file. 


