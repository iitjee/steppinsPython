Most computers spend a lot of time doing nothing. If you start a system monitor tool and watch the CPU utilization, you’ll see 
what I mean—it’s rare to see one hit 100 percent, even when you are running multiple programs.* There are just too many delays 
built into software: disk accesses, network traffic, database queries, waiting for users to click a button, and so on. In 
fact, the majority of a modern CPU’s capacity is often spent in an idle state; faster chips help speed up performance demand 
peaks, but much of their power can go largely unused.


Early on in computing, programmers realized that they could tap into such unused processing power by running more than one 
program at the same time. By dividing the CPU’s attention among a set of tasks, its capacity need not go to waste while any 
given task is waiting for an external event to occur. The technique is usually called parallel processing (and sometimes 
“multiprocessing” or even “multitasking”) because many tasks seem to be performed at once, overlapping and parallel in time. 
It’s at the heart of modern operating systems, and it gave rise to the notion of multiple-active-window computer interfaces 
we’ve all come to take for granted.

here are two fundamental ways to get tasks running at the same time in Python— process forks and spawned threads. 
Functionally, both rely on underlying operating system services to run bits of Python code in parallel. Procedurally, they are 
very dif- ferent in terms of interface, portability, and communication.
for eg: direct process forks are not supported on Windows under standard Python whereas Python’s thread support works on all 
major platforms. 


in this chapter is on introducing more direct techniques—forks, threads, pipes, signals, sockets, and other launching 
techniques—and on using Py- thon’s built-in tools that support them, such as the os.fork call and the threading, queue, and 
multiprocessing modules. 

External Tools (3rd Party):
 MPI for Python system allows Python scripts to also employ the Message Passing Interface (MPI) standard, allowing Python 
programs to exploit multiple processors in various way
