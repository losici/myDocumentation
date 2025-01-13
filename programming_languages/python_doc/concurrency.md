# Concurrency
Concurrency is the execution of multiple instruciton sequences at the same time. The order of execution should not influence the eventual outcomes. The concurrent instrucitons should share the least of shared resources, because the more resources are shared the more coordination you need. 
There are two main of concurrencies:
1. Parallel programming: split a computetional taks in multiple sub-tasks which are assigned to multiple threads or processors that will be executed for other programs. With single-threaded code if you have multople processor in your system only one core is charged with the task and the others are idle or execute instrucitons ofr other programs. With parallel programming all the processors core can e engaged. best suited for CPU intensive task, which is like solving a problem rather than writing/reading for a device.
2. Async programming: reading/writing from/to devices - IO - then this method is more suitable. It works by delegating a subtask to another actor and then it continues to do another work instead of waiting.  When that task is completed,  a callaback function notifies the main thread. 
example: database, web services, copying, downloading data

## Modules
- threading
- multiprocessing
- asyincio

# Asynchronous Programming
## Single Threaded Asyncrony
Usually to run multiple tasks simultaneously you need an array of threads.
Single thread - IO: waiting-executing-waiting, they are linked to Event Driven Architecture. 
IObound tasks are typicallty handled by multiple threads. Each thread is handling a task. A more efficient solution is to have one thread handling more tasks. When one thread is waiting for data, instead of blocking it will switch to another task which is ready to execute. 
Event of loop - responsible for getting items from an ecent queue and handling it.

## Python event loop
Some keywords: `await`, `async`. Execute a courotine ucntion returns the courotin object, to execute a couroutine object you have to wrap it in a future object.

### Future methods
- cancel()
- done()
- result()
- exception()
- add_done_callback()

### Other methods
- await future # pause the executio until future is done
- loop.run_until_complete()
- asyincio.ensure_future()

the asyncio.Future is non-blocking, while concurrent.future.Future it uses traditional concurrancy and so blocking.
