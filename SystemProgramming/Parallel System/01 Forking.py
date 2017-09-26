Forked processes are a traditional way to structure parallel tasks, and they are a fun- damental part of the Unix tool set. 
Forking is based on the notion of copying programs: when a program calls the fork routine, the operating system makes a new 
copy of that program and its process in memory and starts running that copy in parallel with the original. 

Some systems don’t really copy the original program (it’s an expensive operation), but the new copy works as if it were a 
literal copy.

 After a fork, original process = parent and the copy created by os.fork = child
  In general, parents can make any number of children, and children can create child processes of their own; all forked 
processes run independently and in parallel under the operating system’s control, and children may continue to run after their 
parent exits.
  '
  
  
"This script forks child processes until you type 'q'"
      import os
      
      def child():
        print('Hello from child', os.getpid()) 
        os._exit(0) # else goes back to parent loop
        
      def parent(): 
        while True:
          newpid = os.fork() 
          
          if newpid == 0: #this is from child process
            child()
            
          else: #this is from parent process
            print('Hello from parent', os.getpid(), newpid) 
          if input() == 'q': break
      parent()

Python’s process forking tools, available in the os module, are simply thin wrappers over standard forking calls in the 
system library also used by C language programs. 
 **To start a new, parallel process, call the os.fork built-in function. Because this function generates a copy of the 
calling program, it returns a different value in each copy: zero in the child process and the process ID of the new child in 
the parent.
Programs generally test this result to begin different processing in the child only; this script, for instance, 
runs the child function in child processes only.

Because forking is ingrained in the Unix programming model, this script works well on Unix, Linux, and modern Macs. (won’t 
work on the standard version of Python for Windows today, because fork is too much at odds with the Win- dows model. multi 
processing module, provides an alternative for running processes portably )
Note: Above script does work on Windows, however, if you use the Python shipped with the Cygwin system (or build one of your 
own from source-code with Cygwin’s libraries). Cygwin is a free, open source system that provides full Unix-like 
functionality for Windows 

A subtle point: the child process function is also careful to exit explicitly with an os._exit call. We’ll discuss this call 
 in more detail later in this chapter, but if it’s not made, the child process would live on after the child function r
 eturns (remember, it’s just a copy of the original process). The net effect is that the child would go back to the loop in 
 parent and start forking children of its own (i.e., the parent would have grandchildren). If you delete the exit call and 
 rerun, you’ll likely have to type more than one q to stop, because multiple processes are running in the parent function.
 
 
in above eg, each process exits very soon after it starts, so there’s little overlap in time. Let’s do something slightly 
more sophisticated to better illustrate multiple forked processes running in parallel. 

"""
fork basics: start 5 copies of this program running in parallel with the original; each copy counts up to 5 on the same 
stdout stream--forks copy process memory, including file descriptors; fork doesn't currently work on Windows without Cygwin: 
use os.spawnv or multiprocessing on Windows instead; spawnv is roughly like a fork+exec combination;
"""
import os, time

def counter(count):
	for i in range(count):
		time.sleep(1)
		print('[%s] => %s' % (os.getpid(), i))
	
 for i in range(5): 
  pid = os.fork()
		if pid != 0:
			print('Process %d spawned' % pid)
		else: 
   counter(5)
			os._exit(0) 
   print('Main process exiting.')
	# run in new process # simulate real work
	# in parent: continue
	# else in child/new process # run function and exit
	# parent need not wait
 
When run, this script starts 5 processes immediately and exits. All 5 forked processes check in with their first count 
display one second later and every second thereafter. Notice that child processes continue to run, even if the parent 
process that created them terminates:
 The output of all of these processes shows up on the same screen, because all of them share the standard output stream (and 
a system prompt may show up along the way, too). 
 
 Technically, a forked process gets a copy of the original process’s global memory, including open file descriptors. Because 
of that, global objects like files start out with the same values in a child process, so all the processes here are tied to 
the same single stream. But it’s important to remember that global memory is copied, not shared; if a child process changes 
a global object, it changes only its own copy. (As we’ll see, this works differently in threads,
 
