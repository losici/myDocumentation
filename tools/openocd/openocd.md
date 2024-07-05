# OpenOCD Practical guide
OpenOCD (Open On-Chip Debugger) is a tool used for debugging, in-system programming, and boundary-scan testing of embedded systems. It supports various interfaces, such as JTAG, SWD, and others, and can connect to target devices through different hardware adapters. Here's a practical guide on the basics of OpenOCD, including its ports and how to connect to it using telnet or GDB.

## Ports Used by OpenOCD
OpenOCD typically uses three main ports:

1. GDB Port: Default is 3333. This port is used for the GNU Debugger (GDB) to connect to OpenOCD for debugging purposes.
1. Telnet Port: Default is 4444. This port is used to provide a command-line interface to OpenOCD, where you can issue various commands to control the debugger.
1. TCL RPC Port: Default is 6666. This port is used for remote procedure calls using the TCL scripting language.

### Telnet
Telnet is a network protocol used to provide a bidirectional interactive text-oriented communication facility using a virtual terminal connection. It allows a user to log into another computer over a network and provides a command-line interface to interact with the remote system.

Key Points about Telnet
Protocol:

Telnet operates over TCP (Transmission Control Protocol) and typically uses port 23. However, for specific applications like OpenOCD, it can use different ports, such as 4444 for OpenOCD's telnet interface.
Usage:

Telnet can be used to access and manage network devices, servers, and other systems remotely.
It is commonly used for debugging, testing, and configuration tasks, especially in embedded systems and network equipment.
Security:

Telnet is not secure because it transmits data, including passwords, in plain text. This makes it susceptible to eavesdropping and other attacks.
For secure communication, SSH (Secure Shell) is recommended as it encrypts the data transmitted between the client and the server.

For better security, it is recommended to use SSH (Secure Shell) for remote access and management tasks. SSH encrypts all data transmitted over the network, providing a secure communication channel.

To summarize, telnet is a protocol for accessing remote systems via a command-line interface, but it is not secure. For tasks involving OpenOCD, telnet can be useful for issuing commands and managing debugging sessions, but be mindful of its security limitations and consider using SSH where possible.

### TCL RPC Port (Default: 6666)
TCL (Tool Command Language) RPC (Remote Procedure Call) port is used for scripting and automation tasks. OpenOCD can execute TCL scripts via this port.