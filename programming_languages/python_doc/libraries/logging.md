# Logging Module

Consider using the logging module instead of print() because it might provide flexibility, configurability, and better control over how messages are recorded

logging provides multiple levels of severity:

DEBUG – Detailed information, useful for debugging.
INFO – General messages to indicate normal operation.
WARNING – Something unexpected happened, but the program can continue.
ERROR – A serious issue that caused a failure.
CRITICAL – A severe issue that may cause the program to stop.

to that you can use 
```py
import logging

logging.basicConfig(filename='app.log', level=logging.INFO)
logging.info("This message will be written to app.log")
```