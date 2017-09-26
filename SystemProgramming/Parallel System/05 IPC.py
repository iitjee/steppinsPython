As we saw earlier, when scripts spawn threads,(tasks that run in parallel within the program) they can naturally communicate 
by changing and inspecting names and objects in shared global memory. This includes both accessible variables and attributes, 
as well as referenced mutable objects. As we also saw, some care must be taken to use locks to synchronize access to shared 
items that can be updated concurrently. Still, threads offer a fairly straightforward communication model, and the queue 
module can make this nearly automatic for many programs.

Things aren’t quite as simple when scripts start child processes and independent pro- grams that do not share memory in 
general. If we limit the kinds of communications that can happen between programs, many options are available, most of which 
we’ve already seen in this and the prior chapters. For example, the following simple mecha- nisms can all be interpreted as 
cross-program communication devices:
      • Simple files
      • Command-line arguments
      • Program exit status codes
      • Shell environment variables
      • Standard stream redirections
      • Stream pipes managed by os.popen and subprocess
      
Beyond this set, there are other tools in the Python library for performing Inter-Process Communication (IPC). This includes 
sockets, shared memory, signals, anonymous and named pipes, and more.
    • Signals allow programs to send simple notification events to other programs.
    • Anonymous pipes allow threads and related processes that share file descriptors to pass data, but generally rely on the 
Unix-like forking model for processes, which is not universally portable.
    • Named pipes are mapped to the system’s filesystem—they allow completely unre- lated programs to converse, but are not 
available in Python on all platforms.
    • Sockets map to system-wide port numbers—they similarly let us transfer data be- tween arbitrary programs running on the 
same computer, but also between pro- grams located on remote networked machines, and offer a more portable option.


Other IPC tools are available to Python programmers (e.g., shared memory as provided by the mmap module) search the Python 
manuals and website for more details on other IPC schemes if you’re looking for some- thing more specific

