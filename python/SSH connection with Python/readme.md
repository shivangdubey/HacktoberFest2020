## SSH connection with Python

![image](https://raw.githubusercontent.com/shivangdubey/HacktoberFest2020/c73a2b5db87c7bc9e49b11ab196e433c346b2b4d/python/SSH%20connection%20with%20Python/main.png)

### Understanding pxssh

Pxssh is based on pexpect. It’s class extends pexpect.spawn to specialize setting up SSH connections. I use pxssh frequently for making ssh connections in python.

**Module documentation**

```
import pxssh
help(pxssh)

Help on module pxssh:

NAME
   pxssh

FILE
   /usr/lib/python2.7/dist-packages/pxssh.py

DESCRIPTION
   This class extends pexpect.spawn to specialize setting up SSH connections.
   This adds methods for login, logout, and expecting the shell prompt.
    
   $Id: pxssh.py 513 2008-02-09 18:26:13Z noah $

CLASSES
   pexpect.ExceptionPexpect(exceptions.Exception)
       ExceptionPxssh
   pexpect.spawn(__builtin__.object)
       pxssh
```

### Working of pxssh

pxssh uses the shell prompt to synchronize output from the remote host. In order to make this more robust it sets the shell prompt to something more unique than just $ or #.

This should work on most Borne/Bash or Csh style shells. That means it doesn't support Windows.

### Code

![code](https://raw.githubusercontent.com/shivangdubey/HacktoberFest2020/c73a2b5db87c7bc9e49b11ab196e433c346b2b4d/python/SSH%20connection%20with%20Python/carbon.png)

