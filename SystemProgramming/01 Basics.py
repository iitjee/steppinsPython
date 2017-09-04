We’ll see how to use Python to write system tools, GUIs, database applications, Internet scripts, websites, and more. 
we begin our Python programming tour by exploring the systems application domain—scripts that deal with files, programs, and 
the general environment surrounding a program


most of our examples fall into the category of system tools—programs sometimes called command-line utilities, shell scripts, 
system administration, systems programming

For instance, Python’s ease of use and extensive built-in library make it simple (and even fun) to use advanced system 
tools such as threads, signals, forks, sockets, and their kin; such tools are much less accessible under the obscure syntax 
of shell languages and the slow development cycles of compiled languages. 

By employing Python’s stand- ard library, most system scripts written in Python are automatically portable to all major 
platforms. For instance, you can usually run in Linux a Python directory-processing script written in Windows without 
changing its source code at all—simply copy over the source code. Though writing scripts that achieve such portability 
utopia requires some extra effort and practice, if used well, Python could be the only system scripting tool you need to 
use.
  
  
  In fact, the standard library is so powerful that it is not uncommon to hear Python described as batteries included—a 
  phrase generally credited to Frank Stajano meaning that most of what you need for real day-to-day work is already there 
  for importing.
 In practice, programs become most interesting when they start using services external to the language interpreter: 
 networks, files, GUIs, XML, databases, and so on. All of these are supported in the Python standard library.
  
  >>> import sys, os
  >>> len(dir(sys)) # 65 attributes
  >>> len(dir(os)) # 122 on Windows, more on Unix 122
  >>> len(dir(os.path)) # a nested module within os
  
  
  Most system-level interfaces in Python are shipped in just two modules: sys and os.
  other standard modules belong to this domain too. Among them are the following:
        glob
          For filename expansion
        socket
          For network connections and Inter-Process Communication (IPC)
        threading, _thread, queue
          For running and synchronizing concurrent threads
        time, timeit
          For accessing system time details
        subprocess, multiprocessing
          For launching and controlling parallel processes
        signal, select, shutil, tempfile, and others For various other system-related tasks
          Third-party extensions such as pySerial (a serial port interface), Pexpect (an Expect work-alike for controlling 
cross-program dialogs), and even Twisted (a networking framework) can be arguably lumped into the systems domain as well.
          
          
But by and large, sys and os together form the core of Python’s built-in system tools arsenal.

The os module also attempts to provide a portable programming interface to the un- derlying operating system; its functions 
may be implemented differently on different platforms, but to Python scripts, they look the same everywhere. And if that’s 
still not enough, the os module also exports a nested submodule, os.path, which provides a portable interface to file and 
directory processing tools.

Some handy tools to know about various modules:
  1. import myModule
     sys(myModule)      #returns a list of all attributes of myModule (sub-modules it exports is mainly of our interest)
  2. myModule.__doc__
(note: since __doc__ is an attribute, you can actually seen in sys(myModule) )
    
   3. myModule.__doc__ gives one huge line with special characters in between and therefore not so readable. So you can 
   format this string with `print(myModule.__doc__)`
   
   4. print(myModule.__sys__) cannot deal with scrolling properly. So use, help(myModule)


  
  'sys' manual documents all of the standard library, built-in types and functions, and more. Python’s standard manual set 
also includes a short tutorial, a language reference, ex- tending references, and more.
  
     
