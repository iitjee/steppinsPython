Running Shell Commands from Scripts:

The os module is also the place where we run shell commands from within Python scripts. This concept is intertwined with 
others, such as streams (discussed later)

functions:
  os.system                   Runs a shell command from a Python script
  os.popen                    Runs a shell command and connects to its input or output streams

an alternative module:
  subprocess           provides finer-grained control over streams of spawned shell commands (can be used as anlternative 
                          for above two calls)
                          


          >>> import os 
          >>> os.system('dir /B')                   #dir of win == cd of mac
          >>> os.system('type helloshell.py')       #type  === cat
          >>> os.system('type hellshell.py')  
The 0s at the end of the first two commands here are just the return values of the system call itself (its exit status; zero 
generally means success).




Communicating with shell commands:
 The os.system call simply runs a shell command line, but os.popen also connects to the standard input or output streams of 
the command; we get back a file-like object connected to the com- mand’s output by default (if we pass a w mode flag to 
popen, we connect to the com- mand’s input stream instead). 
  By using this object to read the output of a command spawned with popen, we can intercept the text that would normally 
appear in the console window where a command line is typed:
              >>> open('helloshell.py').read()                           "# a Python program\nprint('The Meaning ofLife')\n"
              
              >>> text = os.popen('type helloshell.py').read() 
              >>> text                                              "# a Python program\nprint('The Meaning of Life')\n"
              
              >>> listing = os.popen('dir /B').readlines()
              >>> listing                       #['helloshell.py\n', 'more.py\n', 'more.pyc\n', 'spam.txt\n', 
                                                  '__init__.py\n']

Here, we first fetch a file’s content the usual way (using Python files), then as the output of a shell type command. 
Reading the output of a dir command lets us get a listing of files in a directory that we can then process in a loop. 
              

they can also be used to launch other Python scripts. Assuming your system search path is set to locate your Python (so that 
you can use the shorter “python” in the following instead of the longer “C:\Python31\python”):
          >>> os.system('python helloshell.py')                       # run a Python program The Meaning of Life

          >>> output = os.popen('python helloshell.py').read()
          >>> output                                                  #'The Meaning of Life\n'
          
          
          

The 'subprocess' module alternative:
in recent releases of Python the subprocess module can achieve the same effect as os.system and os.popen; it generally 
requires extra code but gives more control over how streams are connected and used. This becomes especially useful when 
streams are tied in more complex ways.

similar to os.system(..) === subprocess.call(..)
                >>> import subprocess
                >>> subprocess.call('python helloshell.py')         
                      The Meaning of Life
                      0
                >>> subprocess.call('cmd /C "type helloshell.py"')    
                      # a Python program
                      print('The Meaning of Life')
                      0

                >>> subprocess.call('type helloshell.py', shell=True) 
                      # a Python program
                      print('The Meaning of Life')
                      0
Notice the shell=True in the last command here. This is a subtle and platform- dependent requirement:.....








Besides imitating os.system, we can similarly use this module to emulate the os.popen call used earlier, to run a shell 
command and obtain its standard output text in our script:
                    >>> pipe = subprocess.Popen('python helloshell.py', stdout=subprocess.PIPE)
                    >>> pipe.communicate()
                             (b'The Meaning of Life\r\n', None)
                    >>> pipe.returncode
                              0






                

Here, we connect the stdout stream to a pipe, and communicate to run the command to completion and receive its standard 
output and error streams’ text; the command’s exit status is available in an attribute after it completes. Alternatively, we 
can use other interfaces to read the command’s standard output directly and wait for it to exit (which returns the exit 
status):
>>> pipe = subprocess.Popen('python helloshell.py', stdout=subprocess.PIPE)
>>> pipe.stdout.read()
b'The Meaning of Life\r\n'
>>> pipe.wait()
0


In fact, there are direct mappings from os.popen calls to subprocess.Popen objects:
            >>> from subprocess import Popen, PIPE
            >>> Popen('python helloshell.py', stdout=PIPE).communicate()[0] 
                b'The Meaning of Life\r\n'

            >>> import os
            >>> os.popen('python helloshell.py').read()
            'The Meaning of Life\n'

As you can probably tell, subprocess is extra work in these relatively simple cases. It starts to look better, though, when 
'we need to control additional streams in flexible ways. In fact, because it also allows us to process a command’s error and 
input streams in similar ways

Because more advanced use cases for this 'subprocess' module deal with standard streams, we'll deal later at time of stream 
redirection



Shell command limitations:
keep in mind two limitations of system and popen. First, although these two functions themselves are fairly portable, their 
use is really only as portable as the commands that they run. The preceding examples that run DOS dir and type shell 
commands, for instance, work only on Windows, and would have to be changed in order to run ls and cat commands on Unix-like 
platforms.

Second, it is important to remember that running Python files as programs this way is very different and generally much 
slower than importing program files and calling functions they define. When os.system and os.popen are called, they must 
start a brand- new, independent program running on your operating system (they generally run the command in a new process). 
When importing a program file as a module, the Python interpreter simply loads and runs the file’s code in the same process 
in order to generate a module object. No other program is spawned along the way

There are good reasons to build systems as separate programs, too, But in many cases, imported modules are a faster and more 
direct way to compose systems.

If you plan to use these calls in earnest, you should also know that the os.system call normally blocks—that is, pauses—its 
caller until the spawned command line exits. On Linux and Unix-like platforms, the spawned command can generally be made to 
run independently and in parallel with the caller by adding an & shell background operator at the end of the command line:
        os.system("python program.py arg arg &")
On Windows, spawning with a DOS start command will usually launch the command in parallel too:
        os.system("start program.py arg arg")
        
        
        
os.startfile(..)    #works only on WINDOWS     
    os.startfile("webpage.html")          # open file in your web browser
    os.startfile("document.doc")           # open file in Microsoft Word 
    os.startfile("myscript.py")           # run file with Python
    
The os.popen call does not generally block its caller (by definition, the caller must be able to read or write the file 
object returned) but callers may still occasionally become blocked under both Windows and Linux if the pipe object is closed
—e.g., when gar- bage is collected—before the spawned program exits or the pipe is read exhaustively (e.g., with its read() 
method). As we will see later in this part of the book, the Unix os.fork/exec and Windows os.spawnv calls can also be used 
to run parallel programs without blocking. 



so far: we've discussed os module’s system and popen calls, as well as the subprocess module, also fall under the category 
of program launchers, stream redirectors, and cross-process communication devices,  we’ll defer further details till we discuss 'stream redirection' :) bubye!
