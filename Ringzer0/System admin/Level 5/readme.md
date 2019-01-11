# SysAdmin part 5

__PROBLEM__

Decrypt the oracle encrypted file

User: oracle

ssh oracle@challenges.rinzer0team.com -p 10149

__SOLUTION__

Again using that private key we login into oracle's account. Now if you remember in previous task when we `ls` there was an encrypted file along with `flag.txt`, we have to decrypt that file.

Usually that type of encryption is done using `openssl` so you can simply `grep` for openssl in the existing folder.

What I did was:

```bash
oracle@lxc-sysadmin:~$ ls -la
total 32
dr-x------ 3 oracle oracle 4096 Oct 17 02:57 .
drwxr-xr-x 8 root   root   4096 May 30  2018 ..
lrwxrwxrwx 1 root   root      9 May 30  2018 .bash_history -> /dev/null
-r-x------ 1 oracle oracle  235 Aug 23 02:32 .bash_logout
-r-x------ 1 oracle oracle 3512 Aug 23 02:32 .bashrc
-r-x------ 1 oracle oracle   90 Oct  2 19:42 encflag.txt.enc
-r-x------ 1 oracle oracle   53 Oct  2 19:45 flag.txt
lrwxrwxrwx 1 root   root      9 Oct 17 02:57 .mysql_history -> /dev/null
-r-x------ 1 oracle oracle  780 Aug 23 02:32 .profile
drwx------ 2 oracle oracle 4096 Aug 23 02:51 .ssh
oracle@lxc-sysadmin:~$ cat .profile
# ~/.profile: executed by the command interpreter for login shells.
# This file is not read by bash(1), if ~/.bash_profile or ~/.bash_login
# exists.
# see /usr/share/doc/bash/examples/startup-files for examples.
# the files are located in the bash-doc package.

# the default umask is set in /etc/profile; for setting the umask
# for ssh logins, install and configure the libpam-umask package.
#umask 022

# if running bash
if [ -n "$BASH_VERSION" ]; then
    # include .bashrc if it exists
    if [ -f "$HOME/.bashrc" ]; then
        . "$HOME/.bashrc"
    fi
fi

# set PATH so it includes user's private bin if it exists
if [ -d "$HOME/bin" ] ; then
    PATH="$HOME/bin:$PATH"
fi

alias reveal='openssl enc -aes-256-cbc -a -d -in encflag.txt.enc -k '\''lp6PWgOwDctq5Yx7ntTmBpOISc'\'''
```
Notice the last line there openssl is used for decrypting the file with some key/password but we don't have to run the whole command because it's has an alias `reveal`. Just type reveal and you'll get the flag.

```bash
oracle@lxc-sysadmin:~$ reveal
FLAG-54e7f8d0ea560fa7ed98e832900fc45b
```

FLAG - `FLAG-54e7f8d0ea560fa7ed98e832900fc45b`
