# Software Glossary
[A](#a)
[B](#b)
[C](#c)
[D](#d)
[E](#e)
[S](#s)
[U](#u)

## A
## B
## C
## D


1. Deployment: set of activities to make software available to be distributed and used by others.
## E
### Endianness 
It describes the order in which computer memory stores a sequence of bytes. Endianness can be either big or small, and the adjectives refer to the value stored first. Big-endian is an order in which the big end -- the most significant value in the sequence -- is first, at the lowest storage address. Little-endian is an order in which the little end, the least significant value in the sequence, is first. 

  In a number stored in little-endian fashion, the least significant bytes can stay where they are and new digits are added to the right at a higher address. This means some computer operations might be simpler and faster to perform.
  ```
  number = 0x4F52
  // Big Endian
  address 1000 = 4F
  address 1001 = 52
  // Little Endian
  address 1000 = 52
  address 1001 = 4F
  ```
## N
1. Network Byte Order: refers to the ordering of bytes in network communications, specifically the way multi-byte values, such as integers, are transmitted over a network. This order is also known as "big-endian" byte order. Network Byte Order is used universally in network protocols to ensure that data is understood correctly regardless of the underlying computer architecture. It is a standard practice in protocols like IP (Internet Protocol), TCP (Transmission Control Protocol), and UDP (User Datagram Protocol), helping to maintain consistency and interoperability across different systems and platforms. 
## S
### SSH
Secure Shell 
## U
- **Unix Time**: also known as Unix epoch time, POSIX time, or Unix timestamp, is a system for tracking time that represents the number of seconds that have elapsed since the Unix epoch. The Unix epoch is defined as 00:00:00 UTC on January 1, 1970 (chosen for convenience). This system is widely used in computing, especially in Unix-like operating systems, for time-related functions.

  Representations: Unix time is typically *represented as a single integer* (or a double in some implementations), which counts the number of seconds that have passed since the epoch. For example, the Unix time for 00:00:01 UTC on January 1, 1970, is 1.
  
  TimeZone: Unix time is *independent of time zones*. It represents the same moment in time regardless of where you are in the world. Converting Unix time to human-readable time involves adjusting for the local time zone.
  
  Leap Seconds: Unix time does not account for leap seconds. Therefore, during a leap second, Unix time simply continues to increment as if the leap second does not exist.
  
  Future and Past Dates: Unix time can represent dates both far in the past and far into the future. However, in 32-bit systems, the maximum representable time (known as the Year 2038 problem) is limited to 03:14:07 UTC on January 19, 2038.