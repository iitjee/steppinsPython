Pipes, a cross-program communication device, are implemented by your operating system is available in the Python standard 
library.

 Pipes are unidirectional channels that work something like a shared memory buffer, but with an interface re- sembling a 
simple file on each of two ends. In typical use, one program writes data on one end of the pipe, and another reads that data 
on the other end. Each program sees only its end of the pipes and processes it using normal Python file calls.
 
calls to read a pipe will normally "block" the caller until data becomes available (i.e., is sent by the program on the 
other end) instead of returning an end-of-file indicator. Moreover, read calls on a pipe always return the oldest data 
written to the pipe, resulting in a first-in- first-out model—the first data written is the first to be read. Because of 
such properties, 
pipes are also a way to synchronize the execution of independent programs.

Pipes come in two flavors
  —anonymous and 
  -named. 
Named pipes (often called fifos) are represented by a file on your computer. Because named pipes are really external files, 
the communicating processes need not be related at all; in fact, they can be independently started programs.
By contrast, anonymous pipes exist only within processes and are typically used in conjunction with process forks as a way to 
link parent and spawned child processes within an application.            Parent and child converse over shared pipe file 
descriptors, which are inherited by spawned processes. Because threads run in the same process and share all global memory in 
general, anonymous pipes apply to them as well.


Anonymous pipe basics:
      import os, time

      def child(pipeout):
        zzz = 0

        while True:
          time.sleep(zzz)         # make parent wait
          msg = ('Spam %03d' % zzz).encode()  # pipes are binary bytes
          os.write(pipeout, msg)  # send to parent
          zzz = (zzz+1) % 5           # goto 0 after 4

      def parent():
        pipein, pipeout = os.pipe()         # make 2-ended pipe

        if os.fork() == 0:         # copy this process
          child(pipeout)          # in copy, run child
        
        else:             # in parent, listen to pipe
          while True:
            line = os.read(pipein, 32)
            print('Parent %d got [%s] at %s' % (os.getpid(), line, time.time()))
      parent()

os.fork call to make a copy of the calling process as usual.  After forking, the original parent process and its child copy 
speak through the two ends of a pipe created with os.pipe prior to the fork. 
The os.pipe call returns a tuple of two file descriptors—the low-level file identifiers representing the input and output 
sides of the pipe.  Be- cause forked child processes get "copies" of their parents’ file descriptors, writing to the pipe’s 
output descriptor in the child sends data back to the parent on the pipe created before the child was spawned.

If you run this, THE PARENT PROCESS WAITS FOR THE CHILD TO SEND DATA ON THE PIPE EACH TIME IT CALLS  os.read. It’s 
almost as if the child and parent act as client and server here—the parent starts the child and waits for it to initiate 
communication.
To simulate differing task durations, the child keeps the parent wait- ing one second longer between messages with 
time.sleep calls, until the delay has reached four seconds. When the zzz delay counter hits 005, it rolls back down to 000 
and starts again.
  notice, 
    pipein, pipeout = os.pipe()
    os.write(pipeout, msg)
    os.read(pipein, 32)
    

    Notice how the parent received a bytes string through the pipe. Raw pipes normally deal in binary byte strings when 
their descriptors are used directly this way with the descriptor-based file tools we met in Chapter 4 (as we saw there, 
descriptor read and write tools in os always return and expect byte strings). That’s why we also have to manually encode to 
bytes when writing in the child—the string formatting operation is not available on bytes. 

As the next section shows, it’s also possible to wrap a pipe descriptor in a text-mode file object, much as we did in the 
file examples in Chap- ter 4, but that object simply performs encoding and decoding automatically on trans- fers; it’s still 
bytes in the pipe.
