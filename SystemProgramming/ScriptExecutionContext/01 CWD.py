1. Current Working Directory:
 os.getcwd lets a script fetch the CWD name explicitly, and os.chdir allows a script to move to a new CWD.
 
 Keep in mind, though, that filenames without full pathnames map to the CWD and have nothing to do with your PYTHONPATH 
setting. 

Technically, a script is always launched from the CWD, not the directory containing the script file. Conversely, imports 
always first search the directory containing the script, not the CWD (unless the script happens to also be located in 
the CWD). Since this distinction is subtle and tends to trip up beginners, let’s explore it in a bit more detail.

When you run a Python script by typing a shell command line such as python dir1\dir2\file.py, the CWD is the directory you 
were in when you typed this command, not dir1\dir2. 
             os.getcwd()       ---> gives current working directory i.e where your terminal is currently pointing to
             
             
On the other hand, Python automatically adds the identity of the script’s home directory to the front of the module search 
path such that file.py can always import other files in dir1\dir2
              sys.path          ---> it gives a list, whose first element is the script file's parent directory

note: if you execute 'sys.path' in an INTERACTIVE TERMINAL (REPL), you'll get ' ' as first element which means the script's
parent directory which's also CWD in this case. 

For obvious reasons, any import statement in a py file will be checked first in script's parent directory and nothing to
do with CWD here. (bcos, sys.path's first element is script's par dir)





