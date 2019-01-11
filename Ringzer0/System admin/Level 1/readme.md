# SysAdmin part 1

__PROBLEM__

Find Trinity password

User: morpheus
Password: VNZDDLq2x9qXCzVdABbR1HOtz

ssh morpheus@challenges.ringzer0team.com -p 10089

__SOLUTION__

We need to find Trinity password. So we start with simple look around and finds out that there are multiple folders for different identity and another person cannot access someone else folder/directory.

After some looking around I decide to look up all the process that were running

```bash
morpheus@lxc-sysadmin:~$ ps
  PID TTY          TIME CMD
26922 pts/4    00:00:00 bash
26928 pts/4    00:00:00 ps
```

It doesn't give anything cool but after reading `man` page for `ps` I found `ps aux` which basically gives `Every process on the system using BSD syntax`

```
morpheus@lxc-sysadmin:/home$ ps aux
USER       PID %CPU %MEM    VSZ   RSS TTY      STAT START   TIME COMMAND
root         1  0.0  0.0  37228  5380 ?        Ss    2018   4:32 /sbin/init
root        38  0.0  0.1 203580 131388 ?       Ss    2018  19:16 /lib/systemd/systemd-journald
root        90  0.0  0.0  28980  2916 ?        Ss    2018   0:47 /usr/sbin/cron -f
syslog      91  0.0  0.0 256392  4264 ?        Ssl   2018   6:01 /usr/sbin/rsyslogd -n
root       156  0.0  0.0  65508  6528 ?        Ss    2018  12:02 /usr/sbin/sshd -D
mysql      170  0.2  0.2 1545560 194620 ?      Ssl   2018  95:46 /usr/sbin/mysqld
root       174  0.0  0.0  15752  2212 pts/2    Ss+   2018   0:00 /sbin/agetty --noclear --keep-baud pts/2 115200 38400 9600 vt220
root       176  0.0  0.0  15752  2212 pts/1    Ss+   2018   0:00 /sbin/agetty --noclear --keep-baud pts/1 115200 38400 9600 vt220
root       177  0.0  0.0  15752  2212 ?        Ss+   2018   0:00 /sbin/agetty --noclear --keep-baud console 115200 38400 9600 vt220
root       178  0.0  0.0  15752  2212 pts/3    Ss+   2018   0:00 /sbin/agetty --noclear --keep-baud pts/3 115200 38400 9600 vt220
root       182  0.0  0.0  15752  2212 pts/0    Ss+   2018   0:00 /sbin/agetty --noclear --keep-baud pts/0 115200 38400 9600 vt220
root      3011  0.0  0.0   4504  1612 ?        S     2018   0:53 /bin/sh /root/files/backup.sh -u trinity -p Flag-7e0cfcf090a2fe53c97ea3edd3883d0d
root      4991  0.0  0.0  49932  3404 ?        SN   Jan10   0:00 su neo -c /bin/monitor
neo       4993  0.0  0.0   4216   612 ?        SNs  Jan10   0:00 /bin/monitor
root     12609  0.0  0.0  49932  3404 ?        SN   Jan09   0:00 su cypher -c python /tmp/Gathering.py
cypher   12611  0.0  0.0  35028  7132 ?        SNs  Jan09   0:00 python /tmp/Gathering.py
cypher   12612  0.0  0.0  21148  3512 pts/6    SNs+ Jan09   0:00 /bin/bash
root     26874  0.0  0.0  90492  6844 ?        SNs  05:23   0:00 sshd: morpheus [priv]
morpheus 26880  0.0  0.0  90492  3224 ?        SN   05:23   0:00 sshd: morpheus@pts/4
morpheus 26881  0.0  0.0  21180  3736 pts/4    SNs  05:23   0:00 -bash
root     26886  0.0  0.0   7288   644 ?        S    05:24   0:00 sleep 10
root     26888  0.0  0.0  45804  2804 ?        S    05:24   0:00 /usr/sbin/CRON -f
root     26889  0.0  0.0   4504   744 ?        Ss   05:24   0:00 /bin/sh -c /root/files/cronjob.sh
root     26890  0.0  0.0  12508  2892 ?        S    05:24   0:00 /bin/bash /root/files/cronjob.sh
root     26892  0.0  0.0   7288   640 ?        S    05:24   0:00 sleep 5
morpheus 26897  0.0  0.0  37364  3316 pts/4    RN+  05:24   0:00 ps aux
```


FLAG - `Flag-7e0cfcf090a2fe53c97ea3edd3883d0d`
