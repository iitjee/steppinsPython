scripts have access to the following sorts of system-level inputs and interfaces:
1. Current working directory
    os.getcwd gives access to the directory from which a script is started, and many file tools use its value implicitly.
2. Command-line arguments
    sys.argv gives access to words typed on the command line that are used to start the program and that serve as script 
inputs.
3. Shell variables
    os.environ provides an interface to names assigned in the enclosing shell (or a parent program) and passed in to the 
script.
4. Standard streams
    sys.stdin, stdout, and stderr export the three input/output streams that are at the heart of command-line shell tools, and 
can be leveraged by scripts with print op- tions, the os.popen call and subprocess module introduced in Chapter 2, the 
io.StringIO class, and more.

Such tools can serve as inputs to scripts, configuration parameters, and so on. In this chapter, we will explore all these 
four context’s tools



