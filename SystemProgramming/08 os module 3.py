Other os Module Exports:


Since most other os module tools are even more difficult to appreciate outside the context of larger appli- cation topics, we’ll postpone a deeper look at them until later chapters. But to let you sample the flavor of this module, here is a quick preview for reference. Among the os module’s other weapons are these:

os.environ        Fetches and sets shell environment variables
os.fork           Spawns a new child process on Unix-like systems
os.pipe           Communicates between programs
os.execlp         Starts new programs
os.spawnv         Starts new programs with lower-level control
os.open           Opens a low-level descriptor-based file
os.mkdir          Creates a new directory
os.mkfifo         Creates a new named pipe
os.stat           Fetches low-level file information
os.remove         Deletes a file by its pathname
os.walk           Applies a function or loop body to all parts of an entire directory tree


Caution: the os module provides a set of file open, read, and write calls, but all of these deal with low-level file access 
and are entirely distinct from Python’s built-in stdio file objects that we create with the built-in open function. You should 
normally use the built-in open function, not the os module, for all but very special file-processing needs (e.g., opening with 
exclusive access file locking)




subprocess, os.popen, and Iterators:
read p101, p102
