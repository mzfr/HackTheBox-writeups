# SysAdmin part 7

__PROBLEM__

Neo is not alone!

User: neo
Password: FLAG of the Level 6

ssh neo@challenges.ringzer0team.com -p 10089

__SOLUTION__

Password: `FLAG-314df4d411ae37f16f590f65da99f3b6`

This one was easy for some reason. After looking here and there I just tried to look into all the process that is going on under `neo`.

```bash
neo@lxc-sysadmin:~$ ps fl -u neo
F   UID   PID  PPID PRI  NI    VSZ   RSS WCHAN  STAT TTY        TIME COMMAND
5  1004 28125 28119  35  15  90492  3224 -      SN   ?          0:00 sshd: neo@pts/5
0  1004 28126 28125  35  15  21176  3732 wait   SNs  pts/5      0:00  \_ -bash
0  1004 28134 28126  35  15  37364  3192 -      RN+  pts/5      0:00      \_ ps fl -u neo
4  1004  4993  4991  35  15   4216   612 hrtime SNs  ?          0:00 /bin/monitor
```
Okay so there is a `monitor` that is running. The best way to get to it is `strace`

```bash
neo@lxc-sysadmin:~$ strace -p 4993
strace: Process 4993 attached
restart_syscall(<... resuming interrupted nanosleep ...>

) = 0
write(-1, "telnet 127.0.0.1 23\n", 20)  = -1 EBADF (Bad file descriptor)
write(-1, "user\n", 5)                  = -1 EBADF (Bad file descriptor)
write(-1, "FLAG-a4UVY5HJQO5ddLc5wtBps48A3\n", 31) = -1 EBADF (Bad file descriptor)
write(-1, "get-cpuinfo\n", 12)          = -1 EBADF (Bad file descriptor)
nanosleep({10, 0},
```

After running strace command you'll have to wait a sec

FLAG - `FLAG-a4UVY5HJQO5ddLc5wtBps48A3`
