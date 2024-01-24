# TWINCAT MODE
1. Config Mode - Blue: you want to be here everytime you do changes to the system
1. Run Mode - Green: when you want to run the tasks and programs
1. Stop Mode - yellow: Exception Mode you never want to be here because you go here when you have runtime problems or exceptions.

Login --> you can watch variables
Start: you start your program

# Data Types


# Other
Dont'use this for debugging, it takes a lot of resources and it is not efficient.
ADSLOGSTR(msgCtrlMask := ADSLOG_MSGTYPE_ERROR OR ADSLOG_MSGTYPE_LOG,
        msgFmtStr := :Hello %s',
        strArg:= 'world!');

ADS = beckhoff middleware protocol.


infosys.beckhoff.com: most of the documentation is here, use the search to look up the different functions
